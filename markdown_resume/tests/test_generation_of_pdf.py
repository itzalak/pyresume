import glob
from os import remove
from os.path import exists

from markdown_resume.md_resume_to_pdf import pdf_resume

DATA_PATH = f'output/resume*.pdf'
PDF_FILE_PATH = glob.glob(DATA_PATH)[0]


def setup_function():
    """Remove PDF file if exists"""

    if exists(PDF_FILE_PATH):
        remove(PDF_FILE_PATH)
        print(f"PDF deleted from {PDF_FILE_PATH}")


def test_generate_pdf_from_defaults():
    assert not exists(PDF_FILE_PATH)

    pdf_resume()
    assert exists(PDF_FILE_PATH)

# TODO: this test needs to be updated after changing way arguments are called
# def test_style_defaults():
#     style = get_style()
#     print(f"STYLE: {style}")
#     assert style == f"../assets/styles/simple-style.css"
