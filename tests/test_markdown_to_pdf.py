import glob
import os
from os import remove
from os.path import exists

import pytest

from css_styles import CssStyles
from default_resume import DefaultResume
from markdown_to_pdf import generate_pdf, main
from settings import MODULE_DIR

OUTPUT_DATA_PATH = f'{MODULE_DIR}/../output/resume*.pdf'
RESUME = DefaultResume.default_resume_path
DEFAULT_STYLE = CssStyles.default_style


def setup_function():
    """Remove PDF file if exists"""

    asset_path = glob.glob(f'{MODULE_DIR}/../output/*.pdf')
    if asset_path:
        pdf_file_path = asset_path[0]
        if exists(pdf_file_path):
            remove(pdf_file_path)
            print(f"PDF deleted from {pdf_file_path}")


def teardown_function():
    """Remove PDF file if exists"""

    asset_path = glob.glob(f'{MODULE_DIR}/../output/*.pdf')
    if asset_path:
        pdf_file_path = asset_path[0]
        if exists(pdf_file_path):
            remove(pdf_file_path)
            print(f"PDF deleted from {pdf_file_path}")


def test_generate_pdf_from_given_style_file():
    path = os.path.join(MODULE_DIR, "../tests/data/test-style.css")
    generate_pdf(path, RESUME)

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_from_defaults():
    generate_pdf(DEFAULT_STYLE, RESUME)

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_simple_style():
    generate_pdf(CssStyles.simple_style, RESUME)

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_bar_style():
    generate_pdf(CssStyles.bar_style, RESUME)

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_divider_style():
    generate_pdf(CssStyles.divider_style, RESUME)

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_generate_pdf_from_input_markdown_file():
    input_file = os.path.join(MODULE_DIR, '../tests/data/test-markdown-file.md')
    generate_pdf(CssStyles.divider_style, input_file)

    asset_path = os.path.join(MODULE_DIR, '../output/test-markdown-file.pdf')
    assert exists(asset_path)


def test_failure_file_not_markdown():
    input_file = os.path.join(MODULE_DIR, '../tests/data/non-existent-file.mk')

    with pytest.raises(ValueError, match=r'File must be from type markdown, instead \.[a-z]+ was found'):
        generate_pdf(CssStyles.divider_style, input_file)


def test_main_input_css_file():
    input_file = os.path.join(MODULE_DIR, "../tests/data/test-style.css")
    main(input_file, RESUME)

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_main_input_markdown_file():
    input_file = os.path.join(MODULE_DIR, '../tests/data/test-markdown-file.md')
    main(CssStyles.divider_style, input_file)

    asset_path = os.path.join(MODULE_DIR, '../output/test-markdown-file.pdf')
    assert exists(asset_path)


def test_default_main_call():
    main(CssStyles.default_style, DefaultResume.default_resume_path)

    asset_path = glob.glob(OUTPUT_DATA_PATH)[0]
    assert exists(asset_path)


def test_system_exit_css_not_found():
    input_file = os.path.join(MODULE_DIR, 'non-existent-file.css')

    with pytest.raises(SystemExit):
        main(input_file, RESUME)


def test_system_exit_markdown_not_found():
    input_file = os.path.join(MODULE_DIR, 'non-existent-file.md')

    with pytest.raises(SystemExit):
        main(DEFAULT_STYLE, input_file)


def test_system_exit_file_not_markdown():
    input_file = os.path.join(MODULE_DIR, '../tests/data/non-existent-file.mk')

    with pytest.raises(SystemExit):
        main(DEFAULT_STYLE, input_file)
