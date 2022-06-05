from md2pdf.core import md2pdf

from file_actions import FileActions
from settings import RESUME_PATH


def generate_pdf(style: str):
    """Generate pdf file using a given style based of a resume markdown file"""
    pdf_path = FileActions.resume_path()
    markdown_file = RESUME_PATH

    md2pdf(pdf_path, md_file_path=markdown_file, css_file_path=style)
