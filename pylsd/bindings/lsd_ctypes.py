import ctypes
import os
import sys
import random
import numpy as np
from pathlib import Path

def load_lsd_library():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    libname = 'linux/liblsd.so'
    libdir = 'lib'
    lsdlib = ctypes.cdll[Path(root_dir)/libdir/libname]
    return lsdlib
    
lsdlib = load_lsd_library()
if lsdlib == None:
    raise ImportError('Cannot load dynamic library. Did you compile LSD?')
