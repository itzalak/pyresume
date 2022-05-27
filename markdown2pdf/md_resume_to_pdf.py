import datetime

from md2pdf.core import md2pdf

from defaults.default_config import DEFAULT_STYLE, RESUME_PATH, OUTPUT_FOLDER


def get_pdf_filename():
    timestamp = datetime.date.today()
    pdf_filename = f"resume-{timestamp}.pdf"
    return pdf_filename


def get_pdf_path():
    pdf_filename = get_pdf_filename()
    return f"{OUTPUT_FOLDER}/{pdf_filename}"


def pdf_resume(style: str = None):
    if style is None:
        style = DEFAULT_STYLE
    pdf_file_path = get_pdf_path()
    resume_path = RESUME_PATH

    md2pdf(pdf_file_path,
           md_content=None,
           md_file_path=resume_path,
           css_file_path=style,
           base_url=None)


def main(style: str):
    pdf_resume(style)
