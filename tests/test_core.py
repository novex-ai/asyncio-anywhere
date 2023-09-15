import asyncio

import pytest

from asyncio_anywhere import asyncio_run


def test_asyncio_run():
    async def async_fn():
        await asyncio.sleep(0.001)
        return 1

    assert asyncio_run(async_fn()) == 1


def test_asyncio_run_debug():
    async def async_fn():
        await asyncio.sleep(0.001)
        return 1

    assert asyncio_run(async_fn(), debug=True) == 1


def test_invalid_input():
    with pytest.raises(ValueError):
        asyncio_run("not a coroutine")
