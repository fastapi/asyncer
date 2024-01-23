from unittest.mock import patch

import asyncer
import sys
import pytest

if sys.version_info < (3, 11):
    from exceptiongroup import ExceptionGroup

from ...conftest import get_testing_print_function


def test_tutorial():
    calls = []

    new_print = get_testing_print_function(calls)

    with patch("builtins.print", new=new_print):
        with pytest.raises(ExceptionGroup) as e:
            from docs_src.tutorial.soonify_return import tutorial002 as mod

            # Avoid autoflake removing this import
            assert mod  # pragma: nocover
        assert isinstance(e.value.exceptions[0], asyncer.PendingValueException)
    assert calls == []
