from settings import RESUME_PATH, SIMPLE_STYLE, ASSETS_DIR, OUTPUT_DIR, STYLES_DIR, \
    BAR_STYLE, DIVIDER_STYLE, MODULE_DIR


def test_assets_dir_path():
    assert ASSETS_DIR == f"{MODULE_DIR}/assets"


def test_output_folder_path():
    assert OUTPUT_DIR == f"{MODULE_DIR}/../output"


def test_styles_folder_path():
    assert STYLES_DIR == f"{MODULE_DIR}/assets/styles"


def test_simple_style_path():
    assert SIMPLE_STYLE == f"{MODULE_DIR}/assets/styles/simple-style.css"


def test_bar_style_path():
    assert BAR_STYLE == f"{MODULE_DIR}/assets/styles/bar-style.css"


def test_structured_style_path():
    assert DIVIDER_STYLE == f"{MODULE_DIR}/assets/styles/divider-style.css"


def test_resume_path():
    assert RESUME_PATH == f"{MODULE_DIR}/assets/resume.md"
