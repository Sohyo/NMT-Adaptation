import numpy as np
import sys
import csv

csv.field_size_limit(sys.maxsize)

'''
    Prepare dataset to get ready to feed it into the model
    TODO : need to write the more description of functions.
'''

# split the xml file into 2 plain text file(source/target)
def split_into_src_trg(text_path):

    source, target = [], []
    src_text, trg_text = '', ''
    start_point = ">"

    with open(text_path) as f:
        for line in f:
            if line.startswith('(src)'):
                if src_text == '':  # when it is the starting point of the sentence(or text)
                    src_text = line[line.index(start_point) + len(start_point):][:-1]
                else:   # When there are several pieces of sentences, join them with blanks
                    src_text = ' '.join([src_text, line[line.index(start_point) + len(start_point):][:-1]])
                # src_text += line[line.index(start_point) + len(start_point):][:-1]
            elif line.startswith('(trg)'):
                if trg_text == '':  # when it is the starting point of the sentence(or text)
                    trg_text = line[line.index(start_point) + len(start_point):][:-1]
                else:   # When there are several pieces of sentences, join them with blanks
                    trg_text = ' '.join([src_text, line[line.index(start_point) + len(start_point):][:-1]])
            elif line.startswith('==========='):    # finish saving the sentence as a block
                source.append(src_text)
                target.append(trg_text)
                src_text = ''
                trg_text = ''
    return source[1:], target[1:]


def split_datasets(arr, n_train, n_valid, n_test):
    total_num = len(arr)
    if n_train+n_valid+n_test <= total_num:
        train_set, valid_set, test_set = arr[:n_train], arr[n_train:n_valid+n_train], \
                                         arr[n_valid+n_train:n_valid+n_train+n_test]
    return train_set, valid_set, test_set


def format_filename(lang, sets):
    return ".".join(map(str, [sets] + [lang]))
