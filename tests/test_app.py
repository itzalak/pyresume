from pathlib import Path
import toml
import version


def test_version():
    with Path("pyproject.toml").open(encoding="utf8") as toml_file:
        pyproject_toml = toml.load(toml_file)

    poetry_version = pyproject_toml["tool"]["poetry"]["version"]
    pyresume_version = version.PACKAGE_VERSION
    assert f"v{poetry_version}" == pyresume_version
