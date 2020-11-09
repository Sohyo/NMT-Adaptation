from os import listdir
from os.path import isfile, join, getsize
from numpy import column_stack
import re


def get_sorted_file_list_by_size(files_path):
    file_list = [f for f in listdir(files_path) if isfile(join(files_path, f))]
    file_list.sort(key=lambda filename: getsize(join(files_path, filename)), reverse=True)
    return file_list


def get_sorted_file_list_by_name(files_path):
    file_list = [f for f in listdir(files_path) if isfile(join(files_path, f))]
    file_list.sort(key=lambda f: float(re.sub("\D", "", f)))
    return file_list


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
    assert isinstance(join_arr, object)
    return join_arr


def rm_dupl_from_list(doc_in_datasets):
    selected_docs = []
    for doc in doc_in_datasets:
        if doc not in selected_docs:
            selected_docs.append(doc)
    return selected_docs
