import re

from markdown_resume.utils import default_config

PDF_FILENAME_PATTERN = r"resume-\d{4}-\d{2}-\d{2}.pdf"
OUTPUT_PATH = f"output/"
STYLES_PATH = f"assets/styles"
DEFAULT_STYLE = f"assets/styles/simple-style.css"
RESUME_PATH = f"assets/resume.md"


def test_pdf_filename():
    pattern = re.compile(PDF_FILENAME_PATTERN, re.IGNORECASE)

    pdf_filename = default_config.get_pdf_filename()
    assert pattern.search(pdf_filename)


def test_pdf_path():
    pdf_path = OUTPUT_PATH.join({PDF_FILENAME_PATTERN})
    pattern = re.compile(pdf_path, re.IGNORECASE)

    pdf_path = default_config.get_pdf_path()
    assert pattern.search(pdf_path)


def test_default_style():
    default_style = default_config.get_default_style()
    assert default_style == DEFAULT_STYLE


def test_styles_folder_path():
    default_style = default_config.get_styles_path()
    assert default_style == STYLES_PATH


def test_resume_path():
    default_style = default_config.get_resume_path()
    assert default_style == RESUME_PATH

# def test_resume_markdown_file_exists():
#     assert exists(f"../../../assets/resume.md")
#

# def test_styles_exist():
#     assert exists(f'../../assets/styles/simple-style.css')
#     assert exists(f'../../assets/styles/bar-style.css')
#     assert exists(f'../../assets/styles/structurdd-style.css')
