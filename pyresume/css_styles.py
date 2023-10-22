import os

from settings import STYLES_DIR


class CssStyles:
    bar_style = os.path.join(STYLES_DIR, "bar-style.css")
    divider_style = os.path.join(STYLES_DIR, "divider-style.css")
    simple_style = os.path.join(STYLES_DIR, "simple-style.css")
    default_style = simple_style

    @staticmethod
    def stylenames():
        """Get all style names without extension"""
        default_styles = os.listdir(STYLES_DIR)
        style_names = [s.replace(".css", "") for s in default_styles]
        return sorted(style_names)

    @classmethod
    def print_styles(cls):
        """List all styles in a pretty format."""

        style_names = cls.stylenames()
        print("\033[1;32mDefault styles\033[0m:")
        print(" >", "\n > ".join(t for t in style_names))
