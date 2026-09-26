"""Small smoke tests for the beginner-friendly Streamlit app."""

from pathlib import Path

from streamlit.testing.v1 import AppTest

APP_PATH = Path(__file__).resolve().parent.parent / "app.py"


def test_app_starts_without_errors() -> None:
    """The first screen renders successfully."""
    app_test = AppTest.from_file(str(APP_PATH), default_timeout=10)
    app_test.run()

    assert not app_test.exception
    assert app_test.title[0].value == "OCR Text Scanner"
