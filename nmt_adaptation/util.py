from os import listdir
from os.path import isfile, join, getsize
from numpy import column_stack
import re
import numpy as np


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


def adjust_length_2docs(arr_de, arr_en):
    if len(arr_de) == len(arr_en):
        return arr_de, arr_en
    else:
        doc_length = min(len(arr_de), len(arr_en))
        return arr_de[:doc_length], arr_en[:doc_length]


def cleanup_datasets(temp_dir, save_dir):
    # First, get sorted every file names from 'temp_dir'
    file_list = get_sorted_file_list_by_name(temp_dir)

    # Due to it is parallel corpora, need to divide the num of files by 2
    for file_num in range(int(len(file_list)/2)):
        np_de, np_en = np.array([]), np.array([])

        # If one of the corpus has shorter than the other, remove the left sentences from the longer corpus
        de, en = adjust_length_2docs(text2arr(join(temp_dir, str(file_num) + ".de")), text2arr(join(temp_dir, str(file_num)+".en")))
        np_de = np.append(np_de, de, 0)
        np_en = np.append(np_en, en, 0)
        two_lang_docs = np.column_stack((np_de, np_en))

        # Save the brand new both language corpora
        new_de = []
        new_en = []
        for sentences in two_lang_docs:
            if "" not in sentences:
                if len(sentences[0].split()) > 6 and len(sentences[1].split()) > 6:
                    new_de.append(sentences[0])
                    new_en.append(sentences[1])
        arr2txt(new_de, join(save_dir, str(file_num) + ".de"))
        arr2txt(new_en, join(save_dir, str(file_num) + ".en"))
