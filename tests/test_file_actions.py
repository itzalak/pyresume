import os

import pytest

from file_actions import FileActions
from settings import MODULE_DIR


def test_successful_locate_dir():
    assert FileActions.locate_directory(os.path.join(MODULE_DIR, '../output'))


def test_failed_locate_dir():
    assert not FileActions.locate_directory('some-folder')


def test_successful_locate_file():
    FileActions.locate_file(os.path.join(MODULE_DIR, '../tests/data/test-markdown-file.md'))


def test_failed_locate_file():
    with pytest.raises(FileNotFoundError, match=r'No file was found on path: some-name.markdown'):
        FileActions.locate_file('some-name.markdown')


def test_successful_replacement_of_md_extension():
    pdf_path = FileActions.replace_extensions_markdown_for_pdf('some-name.md')
    assert pdf_path == 'some-name.pdf'


def test_successful_replacement_of_markdown_extension():
    pdf_path = FileActions.replace_extensions_markdown_for_pdf('some-name.markdown')
    assert pdf_path == 'some-name.pdf'


def test_failure_for_non_markdown_file():
    with pytest.raises(ValueError, match=r'File must be from type markdown, instead \.[a-z]+ was found'):
        FileActions.replace_extensions_markdown_for_pdf('some-name.txt')


def test_successful_pdf_output_path():
    some_path = os.path.join(MODULE_DIR, '../output/some-name.pdf')

    pdf_path = FileActions.build_output_path('/test/data/some-name.md')
    assert pdf_path == some_path


def test_failure_generating_pdf_output_path():
    with pytest.raises(ValueError, match=r'File must be from type markdown, instead \.[a-z]+ was found'):
        FileActions.replace_extensions_markdown_for_pdf('some-name.bak')
