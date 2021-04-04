from .bindings.lsd_ctypes import lsdlib
import ctypes
import os

def lsd(src):

    rows, cols = src.shape
    src = src.reshape(1, rows * cols).tolist()[0]

    tmp = os.path.abspath('ntl.txt')
    src = (ctypes.c_double * len(src))(*src)
    lsdlib.lsdGet(src, ctypes.c_int(rows), ctypes.c_int(cols), tmp)

    with open(tmp, 'r') as fp:
        cnt = fp.read().strip().split(' ')
    os.remove(tmp)

    count = int(cnt[0])
    dim = int(cnt[1])
    lines = np.array([float(each) for each in cnt[2:]])
    lines = lines.reshape(count, dim)

    return lines
