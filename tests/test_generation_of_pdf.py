import glob
import os
from os import remove
from os.path import exists

from markdown_to_pdf import generate_pdf
from settings import SIMPLE_STYLE, BAR_STYLE, DIVIDER_STYLE, MODULE_DIR

DATA_PATH = f'output/resume*.pdf'


def setup_function():
    """Remove PDF file if exists"""

    asset_path = glob.glob(DATA_PATH)
    if asset_path:
        pdf_file_path = asset_path[0]
        if exists(pdf_file_path):
            remove(pdf_file_path)
            print(f"PDF deleted from {pdf_file_path}")


def test_generate_pdf_from_given_style_file():
    path = os.path.join(MODULE_DIR, "../tests/data/test-style.css")
    generate_pdf(path)

    asset_path = glob.glob(DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_from_defaults():
    generate_pdf(None)

    asset_path = glob.glob(DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_simple_style():
    generate_pdf(SIMPLE_STYLE)

    asset_path = glob.glob(DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_bar_style():
    generate_pdf(BAR_STYLE)

    asset_path = glob.glob(DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_divider_style():
    generate_pdf(DIVIDER_STYLE)

    asset_path = glob.glob(DATA_PATH)[0]
    assert exists(asset_path)
