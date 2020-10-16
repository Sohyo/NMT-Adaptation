from os import listdir
from os.path import isfile, join
from numpy import column_stack
import re

def get_sorted_file_list(files_path):
    xces_file_list = [f for f in listdir(files_path) if isfile(join(files_path, f))]
    # xces_file_list.sort(key=lambda f: int(f[:-4]))
    xces_file_list.sort(key=lambda f: int(re. sub('\D', '', f)))
    return xces_file_list


def text2arr(text_path):
    with open(text_path) as f:
        arr_from_text = [line.rstrip() for line in f]
    return arr_from_text


def arr2txt(arr, file_name):
    with open(file_name, "w") as txt_file:
        for line in arr:
            txt_file.write("".join(line) + "\n")


def join_arrays(source, target):
    join_arr = column_stack((source, target))
    return join_arr