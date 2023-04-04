import os.path as osp


# 문제(1)
def get_max(arr):
    if len(arr) == 0: 
        return None 
    max_val = arr[0] 
    for i in range(1, len(arr)): 
        if arr[i] > max_val: 
            max_val = arr[i]
    return max_val if max_val is not None else 0


def get_min(arr):
    if len(arr) == 0: 
        return None 
    min_val = arr[0] 
    for i in range(1, len(arr)): 
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val if min_val is not None else 0


def get_sum(arr):
    s = 0
    for i in range(len(arr)):
        s += arr[i]
    return s if len(arr) > 0 else 0


def get_mean(arr):
     = len(arr)
    if n == 0:
        return 0
    s = 0
    for i in range(n):
        s += arr[i]
    return s / n


def get_median(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]


# 문제(2)
def count_files(paths):
    """
    paths: 디렉토리 및 파일 경로들이 포함되어 있는 list 객체.
    """
    n_files = 0
    fpaths = set(filter(lambda p: osp.splitext(p)[1] != '', paths))
    for path in paths:
        if path not in fpaths:
            dirname = osp.dirname(path)
            if dirname in fpaths:
                n_files += 1
    return n_files


def filter_fname(fpaths, word):
    """
    fpaths: 파일 경로들이 포함되어 있는 list 객체.
    word: 파일 이름에 포함되어야 하는 단어.
    """
    fpaths_filtered = []
    for path in fpaths:
        fname = osp.basename(path)
        if word in fname:
            fpaths_filtered.append(path)
    return fpaths_filtered


def filter_ext(fpaths, ext):
    """
    fpaths: 파일 경로들이 포함되어 있는 list 객체.
    ext: 파일확장자 (예: "jpg", "png")
    """
    fpaths_filtered = []
    for fpath in fpaths:
        basename = osp.basename(fpath)
        if '.' in basename and basename.split('.')[-1] == ext:
            fpaths_filtered.append(fpath)
    return fpaths_filtered


def change_fname(fpaths, old_word, new_word):
    """
    fpaths: 파일 경로들이 포함되어 있는 list 객체.
    old_word: 파일 이름에서 교체 대상이 되는 단어.
    new_word: 파일 이름에 새롭게 추가할 단어.
    """
    fpaths_new = []
    for fpath in fpaths:
        fname = osp.basename(fpath)
        if old_word in fname:
            fname_new = fname.replace(old_word, new_word)
            fpath_new = osp.join(osp.dirname(fpath), fname_new)
            fpaths_new.append(fpath_new)
        else:
            fpaths_new.append(fpath)
    return fpaths_new


def change_dpath(fpaths, dpath):
    """
    fpaths: 파일 경로들이 포함되어 있는 list 객체.
    dpath: 새로운 디렉토리 경로.    
    """
    fpaths_new = []
    for fpath in fpaths:
        fname = osp.basename(fpath)
        fpath_new = osp.join(dpath, fname)
        fpaths_new.append(fpath_new)
    return fpaths_new
