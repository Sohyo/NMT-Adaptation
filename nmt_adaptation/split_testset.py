from nmt_adaptation.util import get_sorted_file_list_by_name, arr2txt, rm_dupl_from_list, text2arr
import re
from os.path import join
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def measure_length_sentences(path_data):
    length_sentences = []
    with open(join(path_data, "test.de")) as text:
        for sentence in text:
            words = sentence.split()
            length_sentences.append(len(words))

    return length_sentences


def get_src_trg(path_data):
    src = arr2txt(join(path_data, "test."+"de"))
    trg = arr2txt(join(path_data, "test."+"de"))
    return src, trg


list_of_data = ['EMEA', 'GNOME', 'JRC']
root_dir = "../data/custom_data"
# for data in list_of_data:
#     list_len_sentence = measure_length_sentences(join(root_dir, data))
#     counts, bins = np.histogram(list_len_sentence, bins=15, range=(0, 150))
#     # print(counts)
#     # print(bins)
#     short = [sent for sent in list_len_sentence if sent < 10]
#     middle = [sent for sent in list_len_sentence if 10 <= sent < 20]
#     long = [sent for sent in list_len_sentence if 20 <= sent]
#     print(f"short : {len(short)} middle : {len(middle)} long : {len(long)}")



name = 'EMEA'
src = text2arr(join(root_dir, name, "test."+"de"))
trg = text2arr(join(root_dir, name, "test."+"en"))
test_EMEA = {
    "name": 'EMEA',
    "src": src,
    "trg": trg
}

# Combine them

list_len_sentence = measure_length_sentences(join(root_dir, name))
new = np.column_stack((src, trg, list_len_sentence))
print()


# short = [sent for  in new if sent < 10]
# print(f"short : {len(short)}")
# middle = [sent for sent in list_len_sentence if 10 <= sent < 20]
# long = [sent for sent in list_len_sentence if 20 <= sent]
# print(f"short : {len(short)} middle : {len(middle)} long : {len(long)}")


#### PLOT ####

# for data in list_of_data:
#     list_len_sentence = measure_length_sentences(join(root_dir, data))
#     counts, bins = np.histogram(list_len_sentence, bins=10, range=(0, 150))
#     print(f'{data} ->')
#     print(f'counts :{counts}')
#     print(f'bins : {bins}')
#     print(f'max : {max(list_len_sentence)}')
#
#     plt.hist(list_len_sentence, bins=100)
#     # plt.axis([0, 140, 0, 250])
#     # axis([xmin,xmax,ymin,ymax])
#     plt.title(data)
#     plt.ylabel('Counts')
#     plt.xlabel('Length of sentence')
#     plt.show()
