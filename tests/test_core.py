import asyncio

from asyncio_anywhere import asyncio_run


def test_run_async():
    async def async_fn():
        await asyncio.sleep(0.001)
        return 1

    assert asyncio_run(async_fn()) == 1
