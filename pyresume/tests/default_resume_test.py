import re

from pyresume.default_resume import DefaultResume
from pyresume.settings import MODULE_DIR, OUTPUT_DIR

FILENAME_PATTERN = r"resume-\d{14}.pdf"
RESUME_PATH = f"{MODULE_DIR}/assets/resume.md"


def test_default_resume_path():
    expected_primary_path = f"{MODULE_DIR}/assets/resume.md"
    expected_fallback_path = f"{MODULE_DIR}/assets/example-resume.md"

    # Test should pass if default_resume_path matches either the primary or fallback path
    assert DefaultResume.default_resume_path in (
        expected_primary_path,
        expected_fallback_path,
    )


def test_build_output_resume_pdf_filename():
    pattern = re.compile(FILENAME_PATTERN, re.IGNORECASE)

    filename = DefaultResume.build_output_resume_filename()
    assert pattern.search(filename)


def test_resume_path():
    path = f"{OUTPUT_DIR}/".join({FILENAME_PATTERN})
    pattern = re.compile(path, re.IGNORECASE)

    pdf_path = DefaultResume.resume_path()
    assert pattern.search(pdf_path)
