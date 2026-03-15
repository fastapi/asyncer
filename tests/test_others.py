import asyncer
import pytest


def test_pending_repr():
    assert str(asyncer._main.Pending) == "AsyncerPending"


def test_soon_value_pending_flag():
    soon_value = asyncer._main.SoonValue()
    assert soon_value.pending is True
    assert soon_value.ready is False

    soon_value._stored_value = "done"
    assert soon_value.pending is False
    assert soon_value.ready is True


def test_soon_value_value_property_before_and_after_ready() -> None:
    soon_value = asyncer._main.SoonValue()

    with pytest.raises(asyncer.PendingValueException, match="still pending"):
        _ = soon_value.value

    soon_value._stored_value = "done"
    assert soon_value.value == "done"
