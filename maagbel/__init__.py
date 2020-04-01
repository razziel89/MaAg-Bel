import os
# Set some environment variables needed by the library if not yet set
__MAABEL_PATH = os.path.dirname(os.path.realpath(__file__))
# The path to some data files needed by the forcefields
__DATA_PATH = os.path.join(__MAABEL_PATH, "data")
if os.environ.get("BABEL_DATADIR", None) is None:
    os.environ["BABEL_DATADIR"] = __DATA_PATH
# The path to some libraries that can be dlopen'd
if os.environ.get("OB_MODULE_PATH", None) is None:
    os.environ["OB_MODULE_PATH"] = __MAABEL_PATH
# Import the C++ functionality
from .cpp import *
