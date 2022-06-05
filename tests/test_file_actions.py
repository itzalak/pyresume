import os
import re

from file_actions import FileActions
from settings import MODULE_DIR

FILENAME_PATTERN = r"resume-\d{4}-\d{2}-\d{2}.pdf"
RESUME_PATH = f"{MODULE_DIR}/assets/resume.md"
OUTPUT_DIR = f"output"


def test_locate_dir():
    assert FileActions.locate_directory(OUTPUT_DIR)


def test_locate_file():
    assert FileActions.locate_file(RESUME_PATH)


def test_create_filename():
    pattern = re.compile(FILENAME_PATTERN, re.IGNORECASE)

    filename = FileActions.create_filename()
    assert pattern.search(filename)


def test_resume_path():
    path = f"{OUTPUT_DIR}/".join({FILENAME_PATTERN})
    pattern = re.compile(path, re.IGNORECASE)

    pdf_path = FileActions.resume_path()
    assert pattern.search(pdf_path)


def test_file_path():
    some_path = os.path.join(MODULE_DIR, "../output/some-name.pdf")

    pdf_path = FileActions.file_path("some-name.md")
    assert pdf_path == some_path
