import glob
import os
from pathlib import Path

import pytest

from pyresume.file_operations import FileOperations
from pyresume.settings import MODULE_DIR, OUTPUT_DIR


def test_successful_locate_dir():
    FileOperations.assert_directory_exists(OUTPUT_DIR)


def test_failed_locate_dir():
    with pytest.raises(
        FileNotFoundError, match=r"No directory was found at path: some-folder"
    ):
        FileOperations.assert_directory_exists("some-folder")


def test_successful_validate_file_exists():
    FileOperations.assert_file_exists(
        os.path.join(MODULE_DIR, "tests/data/test-markdown-file.md")
    )


def test_failed_validate_file_exists():
    with pytest.raises(
        FileNotFoundError, match=r"No file was found at path: some-name.markdown"
    ):
        FileOperations.assert_file_exists("some-name.markdown")


def test_successful_replacement_of_md_extension():
    pdf_path = FileOperations.replace_extensions_markdown_for_pdf("some-name.md")
    assert pdf_path == "some-name.pdf"


def test_successful_replacement_of_markdown_extension():
    pdf_path = FileOperations.replace_extensions_markdown_for_pdf("some-name.markdown")
    assert pdf_path == "some-name.pdf"


def test_failure_for_non_markdown_file():
    with pytest.raises(
        ValueError, match=r"File must be from type markdown, instead \.[a-z]+ was found"
    ):
        FileOperations.replace_extensions_markdown_for_pdf("some-name.txt")


def test_successful_pdf_output_path():
    some_path = os.path.join(MODULE_DIR, "../output/some-name.pdf")

    pdf_path = FileOperations.build_output_path(Path("/test/data/some-name.md"))
    assert pdf_path == some_path


def test_failure_generating_pdf_output_path():
    with pytest.raises(
        ValueError, match=r"File must be from type markdown, instead \.[a-z]+ was found"
    ):
        FileOperations.replace_extensions_markdown_for_pdf("some-name.bak")


def test_remove_pdfs_from_output_dir():
    FileOperations.remove_pdf_files_from_output_dir()
    assert not glob.glob(f"{MODULE_DIR}/../output/*.pdf")
