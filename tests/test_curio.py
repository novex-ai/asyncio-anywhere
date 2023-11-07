import asyncio

import pytest

from asyncio_anywhere import asyncio_run

try:
    import curio  # type: ignore
    curio_loaded = True
except ImportError:
    curio_loaded = False


@pytest.mark.skipif(not curio_loaded, reason="curio not installed")
def test_curio():
    async def nested_asyncio_fn(x):
        await asyncio.sleep(0.001)
        return x

    async def curio_fn(x):
        await curio.sleep(0.001)
        y = asyncio_run(nested_asyncio_fn(x))
        return y

    assert curio.run(curio_fn, 1) == 1
