import os.path as osp


# 문제(1)
def get_max(arr):
    if len(arr) == 0:
        return 0
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
    return 0


def get_min(arr):
    if len(arr) == 0:
        return 0
    min_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val
    return 0


def get_sum(arr):
    # 코드 작성...
    return 0


def get_mean(arr):
    # 코드 작성...
    return 0


def get_median(arr):
    # 코드 작성...
    return 0


# 문제(2)
def count_files(paths):
    """
    paths: 디렉토리 및 파일 경로들이 포함되어 있는 list 객체.
    """
    n_files = 0
    # 코드 작성...
    return n_files


def filter_fname(fpaths, word):
    """
    fpaths: 파일 경로들이 포함되어 있는 list 객체.
    word: 파일 이름에 포함되어야 하는 단어.
    """
    fpaths_filtered = []
    # 코드 작성...
    return fpaths_filtered


def filter_ext(fpaths, ext):
    """
    fpaths: 파일 경로들이 포함되어 있는 list 객체.
    ext: 파일확장자 (예: "jpg", "png")
    """
    fpaths_filtered = []
    # 코드 작성...
    return fpaths_filtered


def change_fname(fpaths, old_word, new_word):
    """
    fpaths: 파일 경로들이 포함되어 있는 list 객체.
    old_word: 파일 이름에서 교체 대상이 되는 단어.
    new_word: 파일 이름에 새롭게 추가할 단어.
    """
    fpaths_new = []
    # 코드 작성...
    return fpaths_new


def change_dpath(fpaths, dpath):
    """
    fpaths: 파일 경로들이 포함되어 있는 list 객체.
    dpath: 새로운 디렉토리 경로.    
    """
    fpaths_new = []

    return fpaths_new
