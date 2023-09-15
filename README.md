# asyncio-anywhere
Python package that makes it easy to run fast asyncio code

Are you trying to run async code in Python and getting the error
"asyncio.run() cannot be called from a running event loop"?
This package makes it easy to run asyncio-based async code in tricky execution environments:

- [IPython](https://ipython.readthedocs.io/en/stable/)-based notebooks (JupyterLab, AWS Sagemaker, Databricks, etc)
- [trio](https://trio.readthedocs.io/en/stable/) applications
- [curio](https://curio.readthedocs.io/en/latest/) applications

It also seamlessly makes use of [uvloop](https://github.com/MagicStack/uvloop):
- using dependency markers to only install it on supported operating systems
- using uvloop without permanently the asyncio event loop policy

Non Features:
- asyncio-where does not [monkey-patch](https://github.com/erdewit/nest_asyncio) the asyncio module.  We want to avoid doing this because it may cause problems in future Python versions

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
