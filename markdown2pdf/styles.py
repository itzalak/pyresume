import os

from settings import STYLES_DIR


def print_styles():
    """List all styles in a pretty format."""

    style_names = get_styles()
    print("\033[1;32mDefault styles\033[0m:")
    print(" >", "\n > ".join(t for t in style_names))


def get_styles():
    """Get all style names without extension"""
    default_styles = os.listdir(STYLES_DIR)
    style_names = [s.replace(".css", "") for s in default_styles]
    return sorted(style_names)
