import sys

from md2pdf.core import md2pdf

from utils.default_config import get_default_style, get_pdf_path, get_resume_path


def get_style():
    css_file_input = get_default_style()
    if len(sys.argv) > 2:
        sys.exit(f'Unexpected arguments found, {len(sys.argv)} arguments were found, 1 was expected.')
    elif len(sys.argv) == 2:
        css_file_input = sys.argv[1]
    return css_file_input


def pdf_resume():
    css_file_path = get_style()
    pdf_file_path = get_pdf_path()
    resume_path = get_resume_path()

    md2pdf(pdf_file_path,
           md_content=None,
           md_file_path=resume_path,
           css_file_path=css_file_path,
           base_url=None)


pdf_resume()
