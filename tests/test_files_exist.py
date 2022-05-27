from os.path import exists

STYLE_PATH = f"markdown2pdf/assets/styles"
RESUME_PATH = f"markdown2pdf/assets/resume.md"


def test_resume_markdown_file_exists():
    assert exists(RESUME_PATH)


def test_simple_style_exists():
    assert exists(f'{STYLE_PATH}/simple-style.css')
    assert exists(f'{STYLE_PATH}/bar-style.css')
    assert exists(f'{STYLE_PATH}/structured-style.css')
