import os
import platform

__version__ = "0.0.2"

HOME = os.getenv("HOME", os.getenv("USERPROFILE"))
XDG_CACHE_DIR = os.getenv("XDG_CACHE_HOME", os.path.join(HOME, ".cache"))
XDG_CONF_DIR = os.getenv("XDG_CONFIG_HOME", os.path.join(HOME, ".config"))

MODULE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(MODULE_DIR, "assets")
STYLES_DIR = os.path.join(ASSETS_DIR, "styles")
OUTPUT_DIR = os.path.join(MODULE_DIR, "../output")

OS = platform.uname()[0]
