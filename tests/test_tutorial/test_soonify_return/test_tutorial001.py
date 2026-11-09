from unittest.mock import patch

from ...conftest import get_testing_print_function


def test_tutorial():
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        from docs_src.tutorial.soonify_return import tutorial001 as mod

        assert mod
    assert calls == [["Hello, Yury"], ["Hello, Nathaniel"], ["Hello, Alex"]]
