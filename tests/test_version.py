from pathlib import Path
import toml
import version


def test_version():
    with Path("pyproject.toml").open(encoding="utf8") as toml_file:
        pyproject_toml = toml.load(toml_file)

    poetry_version = pyproject_toml["tool"]["poetry"]["version"]
    assert f"{poetry_version}" == f"v{version.__version__}"
