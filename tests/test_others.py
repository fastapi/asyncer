import asyncer


def test_pending_repr():
    assert str(asyncer._main.Pending) == "AsyncerPending"
