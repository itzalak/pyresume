from os.path import exists

from css_styles import CssStyles
from settings import MODULE_DIR


def test_simple_style_path():
    style = CssStyles.simple_style
    assert style == f"{MODULE_DIR}/assets/styles/simple-style.css"
    assert exists(style)


def test_bar_style_path():
    style = CssStyles.bar_style
    assert style == f"{MODULE_DIR}/assets/styles/bar-style.css"
    assert exists(style)


def test_structured_style_path():
    style = CssStyles.divider_style
    assert style == f"{MODULE_DIR}/assets/styles/divider-style.css"
    assert exists(style)


def test_default_style_path():
    style = CssStyles.default_style
    assert style == f"{MODULE_DIR}/assets/styles/simple-style.css"
    assert exists(style)


def test_stylenames():
    names = CssStyles.stylenames()

    assert names == sorted(['simple-style', 'bar-style', 'divider-style'])


def test_print_styles_output():
    # TODO: Test presence of stylenames in output?
    pass
