from typing import Any, Callable, Dict, List, Union


def get_testing_print_function(
    calls: List[List[Union[str, Dict[str, Any]]]],
) -> Callable[..., Any]:
    def new_print(*args):
        data = []
        for arg in args:
            data.append(arg)
        calls.append(data)

    return new_print
