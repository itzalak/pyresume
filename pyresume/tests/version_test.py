from pathlib import Path
import toml
from pyresume.version import __version__


def find_project_root(start_path=None):
    """Find the project root by looking for pyproject.toml"""
    if start_path is None:
        start_path = Path(__file__).parent

    current = start_path
    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent

    raise FileNotFoundError("Could not find pyproject.toml in any parent directory")


def test_version():
    project_root = find_project_root()
    pyproject_path = project_root / "pyproject.toml"

    with pyproject_path.open(encoding="utf8") as toml_file:
        pyproject_toml = toml.load(toml_file)

    project_version = pyproject_toml["project"]["version"]
    package_version = __version__
    assert f"v{project_version}" == package_version
