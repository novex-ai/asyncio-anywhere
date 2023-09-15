import asyncio

import curio  # type: ignore

from asyncio_anywhere import run_async


def test_curio():
    async def nested_asyncio_fn(x):
        await asyncio.sleep(0.001)
        return x

    async def curio_fn(x):
        await curio.sleep(0.001)
        y = run_async(nested_asyncio_fn(x))
        return y

    assert curio.run(curio_fn, 1) == 1
