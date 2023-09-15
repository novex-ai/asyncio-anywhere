import asyncio

from asyncio_anywhere import run_async


def test_run_async():
    async def async_fn():
        await asyncio.sleep(0.001)
        return 1

    assert run_async(async_fn()) == 1
