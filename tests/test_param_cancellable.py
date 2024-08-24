import warnings

import anyio
import pytest
from asyncer import asyncify


def test_cancellable_warns():
    def do_async_work():
        return "Hello World!"

    async def main():
        result = await asyncify(do_async_work, cancellable=True)()
        return result

    with pytest.warns(DeprecationWarning) as record:
        result = anyio.run(main)
    assert isinstance(record[0].message, Warning)
    assert (
        "The `cancellable=` keyword argument to `asyncer.asyncify()` is "
        "deprecated since Asyncer 0.0.8" in record[0].message.args[0]
    )
    assert result == "Hello World!"


def test_abandon_on_cancel_no():
    def do_async_work():
        return "Hello World!"

    async def main():
        result = await asyncify(do_async_work, abandon_on_cancel=True)()
        return result

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        result = anyio.run(main)
    assert result == "Hello World!"
