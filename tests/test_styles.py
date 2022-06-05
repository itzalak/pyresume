from css_styles import CssStyles


def test_stylenames():
    names = CssStyles.stylenames()

    assert names == sorted(['simple-style', 'bar-style', 'divider-style'])


def test_print_styles_output():
    # TODO: Test presence of stylenames in output?
    pass
