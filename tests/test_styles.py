from styles import get_styles


def test_get_styles():
    names = get_styles()

    assert names == sorted(['simple-style', 'bar-style', 'divider-style'])
