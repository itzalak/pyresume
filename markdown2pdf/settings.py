import os
import platform

__version__ = "0.0.1"

HOME = os.getenv("HOME", os.getenv("USERPROFILE"))
XDG_CACHE_DIR = os.getenv("XDG_CACHE_HOME", os.path.join(HOME, ".cache"))
XDG_CONF_DIR = os.getenv("XDG_CONFIG_HOME", os.path.join(HOME, ".config"))

MODULE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(MODULE_DIR, "assets")
STYLES_DIR = os.path.join(ASSETS_DIR, "styles")

SIMPLE_STYLE = os.path.join(STYLES_DIR, "simple-style.css")
BAR_STYLE = os.path.join(STYLES_DIR, "bar-style.css")
DIVIDER_STYLE = os.path.join(STYLES_DIR, "divider-style.css")

RESUME_PATH = os.path.join(ASSETS_DIR, "resume.md")

OUTPUT_DIR = os.path.join(MODULE_DIR, "../output")

OS = platform.uname()[0]
