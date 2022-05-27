import glob
import re
from os import remove
from os.path import exists

from markdown_to_pdf import generate_pdf, get_pdf_filename, get_pdf_path

DATA_PATH = f'output/resume*.pdf'
FILENAME_PATTERN = r"resume-\d{4}-\d{2}-\d{2}.pdf"


def setup_function():
    """Remove PDF file if exists"""

    asset_path = glob.glob(DATA_PATH)
    if asset_path:
        pdf_file_path = asset_path[0]
        if exists(pdf_file_path):
            remove(pdf_file_path)
            print(f"PDF deleted from {pdf_file_path}")


def test_generate_pdf_from_defaults():
    generate_pdf(None)

    asset_path = glob.glob(DATA_PATH)[0]
    assert exists(asset_path)


def test_pdf_filename():
    pattern = re.compile(FILENAME_PATTERN, re.IGNORECASE)

    filename = get_pdf_filename()
    assert pattern.search(filename)


def test_get_pdf_path():
    path = "output/".join({FILENAME_PATTERN})
    pattern = re.compile(path, re.IGNORECASE)

    pdf_path = get_pdf_path()
    assert pattern.search(pdf_path)
