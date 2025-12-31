from typing import Any, Callable, Union


def get_testing_print_function(
    calls: list[list[Union[str, dict[str, Any]]]],
) -> Callable[..., Any]:
    def new_print(*args):
        data = []
        for arg in args:
            data.append(arg)
        calls.append(data)

    return new_print
