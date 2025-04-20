from os.path import exists

import pytest

from pyresume.css_styles import CssStyles
from pyresume.settings import MODULE_DIR


@pytest.fixture(scope="module")
def css_styles():
    return CssStyles()


def test_simple_style_path(css_styles):
    style = css_styles.simple_style
    assert style == f"{MODULE_DIR}/assets/styles/simple-style.css"
    assert exists(style)


def test_bar_style_path(css_styles):
    style = css_styles.bar_style
    assert style == f"{MODULE_DIR}/assets/styles/bar-style.css"
    assert exists(style)


def test_structured_style_path(css_styles):
    style = css_styles.divider_style
    assert style == f"{MODULE_DIR}/assets/styles/divider-style.css"
    assert exists(style)


def test_default_style_path(css_styles):
    style = css_styles.default_style
    assert style == f"{MODULE_DIR}/assets/styles/simple-style.css"
    assert exists(style)


def test_style_names(css_styles):
    names = css_styles.get_styles()

    assert names == sorted(["simple-style", "bar-style", "divider-style"])


def test_print_styles_output(capsys, css_styles):
    css_styles.print_styles()

    captured = capsys.readouterr()
    assert "Available styles" in captured.out
    for style in ["bar-style", "divider-style", "simple-style"]:
        assert style in captured.out
