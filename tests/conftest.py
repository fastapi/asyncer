from collections.abc import Callable
from typing import Any


def get_testing_print_function(
    calls: list[list[str | dict[str, Any]]],
) -> Callable[..., Any]:
    def new_print(*args):
        data = []
        for arg in args:
            data.append(arg)
        calls.append(data)

    return new_print
