import glob
import os
from os import remove
from os.path import exists

import pytest

from pyresume.css_styles import CssStyles
from pyresume.pdf_generator import PdfGenerator
from pyresume.settings import MODULE_DIR

OUTPUT_DATA_PATH = f"{MODULE_DIR}/../output/resume*.pdf"


@pytest.fixture(scope="module")
def css_styles():
    return CssStyles()


@pytest.fixture(scope="module")
def pdf_generator():
    return PdfGenerator()


def setup_function():
    """Remove PDF file if exists"""

    asset_path = glob.glob(f"{MODULE_DIR}/../output/*.pdf")
    if asset_path:
        pdf_file_path = asset_path[0]
        if exists(pdf_file_path):
            remove(pdf_file_path)
            print(f"PDF deleted from {pdf_file_path}")


def teardown_function():
    """Remove PDF file if exists"""

    asset_path = glob.glob(f"{MODULE_DIR}/../output/*.pdf")
    if asset_path:
        pdf_file_path = asset_path[0]
        if exists(pdf_file_path):
            remove(pdf_file_path)
            print(f"PDF deleted from {pdf_file_path}")


def test_generate_pdf_from_given_style_file(pdf_generator):
    path = os.path.join(MODULE_DIR, "tests/data/test-style.css")
    pdf_generator.generate_pdf(path, pdf_generator.default_resume_path)

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_from_defaults(css_styles, pdf_generator):
    pdf_generator.generate_pdf(
        css_styles.default_style, pdf_generator.default_resume_path
    )

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_simple_style(css_styles, pdf_generator):
    pdf_generator.generate_pdf(
        css_styles.simple_style, pdf_generator.default_resume_path
    )

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_bar_style(css_styles, pdf_generator):
    pdf_generator.generate_pdf(css_styles.bar_style, pdf_generator.default_resume_path)

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_divider_style(css_styles, pdf_generator):
    pdf_generator.generate_pdf(
        css_styles.divider_style, pdf_generator.default_resume_path
    )

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_from_input_markdown_file(css_styles, pdf_generator):
    input_file = os.path.join(MODULE_DIR, "tests/data/test-markdown-file.md")
    pdf_generator.generate_pdf(css_styles.divider_style, input_file)

    asset_path = os.path.join(MODULE_DIR, "../output/test-markdown-file.pdf")
    assert exists(asset_path)


def test_failure_file_not_markdown(css_styles, pdf_generator):
    input_file = os.path.join(MODULE_DIR, "tests/data/non-compliant-file.mk")

    with pytest.raises(
        ValueError, match=r"File must be from type markdown, instead \.[a-z]+ was found"
    ):
        pdf_generator.generate_pdf(css_styles.divider_style, input_file)


def test_main_input_css_file(pdf_generator):
    input_file = os.path.join(MODULE_DIR, "tests/data/test-style.css")
    pdf_generator.to_pdf(input_file, pdf_generator.default_resume_path)

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_main_input_markdown_file(css_styles, pdf_generator):
    input_file = os.path.join(MODULE_DIR, "tests/data/test-markdown-file.md")
    pdf_generator.to_pdf(css_styles.divider_style, input_file)

    asset_path = os.path.join(MODULE_DIR, "../output/test-markdown-file.pdf")
    assert exists(asset_path)


def test_default_main_call(css_styles, pdf_generator):
    pdf_generator.to_pdf(css_styles.default_style, pdf_generator.default_resume_path)

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_system_exit_css_not_found(pdf_generator):
    input_file = os.path.join(MODULE_DIR, "non-existent-file.css")

    with pytest.raises(SystemExit):
        pdf_generator.to_pdf(input_file, pdf_generator.default_resume_path)


def test_system_exit_markdown_not_found(css_styles, pdf_generator):
    input_file = os.path.join(MODULE_DIR, "non-existent-file.md")

    with pytest.raises(SystemExit):
        pdf_generator.to_pdf(css_styles.default_style, input_file)


def test_system_exit_file_not_markdown(css_styles, pdf_generator):
    input_file = os.path.join(MODULE_DIR, "../tests/data/non-existent-file.mk")

    with pytest.raises(SystemExit):
        pdf_generator.to_pdf(css_styles.default_style, input_file)
