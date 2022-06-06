from settings import ASSETS_DIR, OUTPUT_DIR, STYLES_DIR, \
    MODULE_DIR


def test_assets_dir_path():
    assert ASSETS_DIR == f"{MODULE_DIR}/assets"


def test_output_folder_path():
    assert OUTPUT_DIR == f"{MODULE_DIR}/../output"


def test_styles_folder_path():
    assert STYLES_DIR == f"{MODULE_DIR}/assets/styles"
