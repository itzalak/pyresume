from markdown2pdf.defaults.default_config import RESUME_PATH, DEFAULT_STYLE, ASSETS_FOLDER, OUTPUT_FOLDER, STYLES_FOLDER


def test_assets_folder_path():
    assert ASSETS_FOLDER == f"markdown2pdf/assets"


def test_output_folder_path():
    assert OUTPUT_FOLDER == f"output"


def test_styles_folder_path():
    assert STYLES_FOLDER == f"markdown2pdf/assets/styles"


def test_default_style_path():
    assert DEFAULT_STYLE == f"markdown2pdf/assets/styles/simple-style.css"


def test_resume_path():
    assert RESUME_PATH == f"markdown2pdf/assets/resume.md"
