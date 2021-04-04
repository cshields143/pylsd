import ctypes
import os
import sys
import random
import numpy as np
from pathlib import Path

DIR = os.path.abspath(os.path.dirname(__file__))
PATH = Path(DIR)/'lib'/'liblsd.so'
lsdlib = ctypes.cdll[str(PATH)]

