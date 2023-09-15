import asyncio

import trio  # type: ignore

from asyncio_anywhere import run_async


def test_trio():
    async def nested_asyncio_fn(x):
        await asyncio.sleep(0.001)
        return x

    async def trio_fn(x):
        await trio.sleep(0.001)
        y = run_async(nested_asyncio_fn(x))
        return y

    assert trio.run(trio_fn, 1) == 1
