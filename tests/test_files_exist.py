from os.path import exists

from settings import MODULE_DIR

STYLE_PATH = f"{MODULE_DIR}/assets/styles"
RESUME_PATH = f"{MODULE_DIR}/assets/resume.md"


def test_resume_markdown_file_exists():
    assert exists(RESUME_PATH)


def test_styles_exists():
    assert exists(f'{STYLE_PATH}/simple-style.css')
    assert exists(f'{STYLE_PATH}/bar-style.css')
    assert exists(f'{STYLE_PATH}/divider-style.css')
