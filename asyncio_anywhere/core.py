import asyncio
import logging
from threading import Thread
from typing import Coroutine, Any

try:
    import uvloop  # type: ignore
except ImportError:
    uvloop_installed = False
else:
    uvloop_installed = True

logger = logging.getLogger(__name__.split(".")[0])
logger.addHandler(logging.NullHandler())


def asyncio_run(coro: Coroutine) -> Any:
    """
    Safely run an async coroutine synchronously (without await).
    Do this irregardless of the current execution environment (IPython-based notebook, script, etc)
    Try to use uvloop for faster i/o if possible
    """
    event_loop = _safe_get_running_loop()
    if event_loop and event_loop.is_running():
        logger.info("event loop already running.  Using thread to bypass.")
        thread = _AsyncRunnerThread(coro)
        thread.start()
        thread.join()
        return thread.result
    else:
        return _fast_asyncio_run(coro)


class _AsyncRunnerThread(Thread):
    """
    adapted from https://stackoverflow.com/a/75094151/22484883
    """

    def __init__(self, coro):
        self.coro = coro
        self.result = None
        super().__init__()

    def run(self):
        self.result = _fast_asyncio_run(self.coro)


def _fast_asyncio_run(coro: Coroutine) -> Any:
    if uvloop_installed:
        pre_existing_policy = asyncio.get_event_loop_policy()
        logger.debug("using uvloop for faster asyncio")
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    else:
        pre_existing_policy = None
    try:
        return asyncio.run(coro)
    finally:
        if pre_existing_policy:
            asyncio.set_event_loop_policy(pre_existing_policy)


def _safe_get_running_loop():
    try:
        return asyncio.get_running_loop()
    except RuntimeError:
        return None
