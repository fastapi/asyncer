from unittest.mock import patch

from ...conftest import get_testing_print_function


def test_tutorial_001():
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        from docs_src.tutorial.first_steps import tutorial001 as mod

        assert mod
    assert calls == [["Hello, World"]]
