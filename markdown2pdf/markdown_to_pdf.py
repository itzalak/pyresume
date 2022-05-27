import datetime

from md2pdf.core import md2pdf

from settings import RESUME_PATH, OUTPUT_DIR


def get_pdf_filename():
    """Create pdf name with timestamp identifier"""
    timestamp = datetime.date.today()
    pdf_filename = f"resume-{timestamp}.pdf"
    return pdf_filename


def get_pdf_path():
    """Create pdf path from pdf name and output dir"""
    pdf_filename = get_pdf_filename()
    return f"{OUTPUT_DIR}/{pdf_filename}"


def generate_pdf(style: str):
    """Generate pdf file using a given style based of a resume markdown file"""
    pdf_file_path = get_pdf_path()
    resume_path = RESUME_PATH

    md2pdf(pdf_file_path,
           md_content=None,
           md_file_path=resume_path,
           css_file_path=style,
           base_url=None)
