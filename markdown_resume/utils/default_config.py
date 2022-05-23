import datetime

ASSETS_FOLDER = f"assets"
OUTPUT_FOLDER = f"output"
STYLES_FOLDER = f"{ASSETS_FOLDER}/styles"
DEFAULT_STYLE = f"{STYLES_FOLDER}/simple-style.css"
RESUME_PATH = f"{ASSETS_FOLDER}/resume.md"


def get_pdf_filename():
    timestamp = datetime.date.today()
    pdf_filename = f"resume-{timestamp}.pdf"
    return pdf_filename


def get_pdf_path():
    pdf_filename = get_pdf_filename()
    return f"{OUTPUT_FOLDER}/{pdf_filename}"


def get_default_style():
    return DEFAULT_STYLE


def get_styles_path():
    return STYLES_FOLDER


def get_resume_path():
    return RESUME_PATH
