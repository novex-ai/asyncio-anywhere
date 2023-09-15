import asyncio

import trio  # type: ignore

from asyncio_anywhere import asyncio_run


def test_trio():
    async def nested_asyncio_fn(x):
        await asyncio.sleep(0.001)
        return x

    async def trio_fn(x):
        await trio.sleep(0.001)
        y = asyncio_run(nested_asyncio_fn(x))
        return y

    assert trio.run(trio_fn, 1) == 1
