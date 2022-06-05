import os

from settings import STYLES_DIR, SIMPLE_STYLE


class CssStyles:
    default_style = SIMPLE_STYLE

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
