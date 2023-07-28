from unittest.mock import patch

from ...conftest import get_testing_print_function


def test_tutorial():
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        from docs_src.tutorial.soonify_return import tutorial003 as mod

        assert mod
    assert calls == [
        ["Preview value1: Hello, Yury"],
        ["Hello, Yury"],
        ["Hello, Nathaniel"],
        ["Hello, Alex"],
    ]
