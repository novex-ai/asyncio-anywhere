# asyncio-anywhere
Python package that makes it easy to run fast asyncio code

[![PyPI version](https://badge.fury.io/py/asyncio-anywhere.svg)](https://badge.fury.io/py/asyncio-anywhere)
[![Release Notes](https://img.shields.io/github/release/novex-ai/asyncio-anywhere)](https://github.com/novex-ai/asyncio-anywhere/releases)
[![pytest](https://github.com/novex-ai/asyncio-anywhere/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/novex-ai/asyncio-anywhere/actions/workflows/pytest.yml)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

Are you trying to run async code in Python and getting the error
`asyncio.run() cannot be called from a running event loop`?
This package makes it easy to run asyncio-based async code in tricky execution environments:

- [IPython](https://ipython.readthedocs.io/en/stable/)-based notebooks (JupyterLab, AWS Sagemaker, Databricks, etc)
- [trio](https://trio.readthedocs.io/en/stable/) applications
- [curio](https://curio.readthedocs.io/en/latest/) applications

Other Features:
- use [uvloop](https://github.com/MagicStack/uvloop) for faster i/o - but without permanently changing the asyncio event loop policy
- type hints to support type-aware IDEs

Non Features:
- asyncio-anywhere does not [monkey-patch](https://github.com/erdewit/nest_asyncio) the asyncio module.  We want to avoid doing this because it may cause problems in future Python versions

## Usage

```sh
pip install asyncio-anywhere
```

```python
import asyncio
from asyncio_anywhere import asyncio_run


async def myfunc():
    await asyncio.sleep(0.01)
    return "OK"


result = asyncio_run(myfunc())

print(result)
```

Use `asyncio_run()` anwhere where you would normally have run [asyncio.run()](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run).
