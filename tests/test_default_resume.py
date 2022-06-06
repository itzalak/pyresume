import re

from default_resume import DefaultResume
from settings import OUTPUT_DIR, MODULE_DIR

FILENAME_PATTERN = r'resume-\d{14}.pdf'
RESUME_PATH = f'{MODULE_DIR}/assets/resume.md'


def test_default_resume_path():
    assert DefaultResume.default_resume_path == f"{MODULE_DIR}/assets/resume.md"


def test_build_output_resume_pdf_filename():
    pattern = re.compile(FILENAME_PATTERN, re.IGNORECASE)

    filename = DefaultResume.build_output_resume_filename()
    assert pattern.search(filename)


def test_resume_path():
    path = f'{OUTPUT_DIR}/'.join({FILENAME_PATTERN})
    pattern = re.compile(path, re.IGNORECASE)

    pdf_path = DefaultResume.resume_path()
    assert pattern.search(pdf_path)
