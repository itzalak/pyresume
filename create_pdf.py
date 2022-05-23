import datetime
import sys

from md2pdf.core import md2pdf


def set_appearance():
    css_file_input = f'assets/styles/simple-style.css'
    if len(sys.argv) > 2:
        sys.exit(f'Unexpected arguments found, {len(sys.argv)} arguments were found, 1 was expected.')
    elif len(sys.argv) == 2:
        css_file_input = sys.argv[1]
    return css_file_input


def build_pdf_filepath():
    timestamp = datetime.date.today()
    return f'output/resume-{timestamp}.pdf'


def pdf_resume():
    css_file_path = set_appearance()
    pdf_file_path = build_pdf_filepath()
    resume_path = 'assets/RESUME.md'

    md2pdf(pdf_file_path,
           md_content=None,
           md_file_path=resume_path,
           css_file_path=css_file_path,
           base_url=None)


pdf_resume()
