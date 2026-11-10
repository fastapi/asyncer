import subprocess
import sys

import asyncer
import pytest


def test_pending_repr():
    assert str(asyncer._main.Pending) == "AsyncerPending"


@pytest.mark.skipif(sys.version_info < (3, 15), reason="typing_extensions is required")
def test_import_without_typing_extensions():
    subprocess.run(
        [
            sys.executable,
            "-I",
            "-c",
            "import sys; sys.modules['typing_extensions'] = None; import asyncer",
        ],
        check=True,
    )
