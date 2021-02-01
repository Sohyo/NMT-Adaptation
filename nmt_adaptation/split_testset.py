from nmt_adaptation.util import arr2txt, rm_dupl_from_list, text2arr
import re
from os.path import join
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def get_length_sentences_from_file(path_data: dir) -> list:
    length_sentences = []
    with open(join(path_data, "test.de")) as text:
        for sentence in text:
            words = sentence.split()
            length_sentences.append(len(words))

    return length_sentences


def get_length_sentences_from_array(arr_sentences: list) -> list:
    length_sentences = []
    for sentence in arr_sentences:
        words = sentence.split()
        length_sentences.append(len(words))

    return length_sentences


def split_testset(test_df: object) -> object:
    short_sentences = test_df.loc[test_df['len_src_sent'] < 10]
    middle_sentences = test_df.loc[(test_df['len_src_sent'] < 20) & (test_df['len_src_sent'] >= 10)]
    long_sentences = test_df.loc[test_df['len_src_sent'] >= 20]
    return short_sentences, middle_sentences, long_sentences


def create_new_testset(test_df, root_dir, data_name):
    short_sentences = test_df.loc[test_df['len_src_sent'] < 10]
    middle_sentences = test_df.loc[(test_df['len_src_sent'] < 20) & (test_df['len_src_sent'] >= 10)]
    long_sentences = test_df.loc[test_df['len_src_sent'] >= 20]

    arr2txt(short_sentences['src'], join(root_dir, data_name, "short_test.de"))
    arr2txt(short_sentences['trg'], join(root_dir, data_name, "short_test.en"))
    arr2txt(middle_sentences['src'], join(root_dir, data_name, "middle_test.de"))
    arr2txt(middle_sentences['trg'], join(root_dir, data_name, "middle_test.en"))
    arr2txt(long_sentences['src'], join(root_dir, data_name, "long_test.de"))
    arr2txt(long_sentences['trg'], join(root_dir, data_name, "long_test.en"))


def create_test_dict(root_dir: dir, data_name: str) -> dict:

    # Get each source and target sentences from the testset file.
    source = text2arr(join(root_dir, data_name, "test." + "de"))
    target = text2arr(join(root_dir, data_name, "test." + "en"))

    # Count all of source(German) sentence lengths.
    list_len_sentence = get_length_sentences_from_file(join(root_dir, data_name))

    # With all the information, create testset dictionary
    test_dict = {
        "name": data_name,
        "src": source,
        "trg": target,
        "len_src_sent": list_len_sentence
    }
    return test_dict


def main():

    root_dir = "../data/custom_data"

    test_GNOME_dict = create_test_dict(root_dir=root_dir, data_name='GNOME')
    test_EMEA_dict = create_test_dict(root_dir=root_dir, data_name='EMEA')
    test_JRC_dict = create_test_dict(root_dir=root_dir, data_name='JRC')

    emea_df = pd.DataFrame(test_EMEA_dict)
    gnome_df = pd.DataFrame(test_GNOME_dict)
    jrc_df = pd.DataFrame(test_JRC_dict)

    create_new_testset(test_df=emea_df, root_dir=root_dir, data_name="EMEA")
    create_new_testset(test_df=gnome_df, root_dir=root_dir, data_name="GNOME")
    create_new_testset(test_df=jrc_df, root_dir=root_dir, data_name="JRC")

    list_of_data = ['EMEA', 'GNOME', 'JRC']
    for data in list_of_data:
        list_len_sentence = get_length_sentences_from_file(join(root_dir, data))
        counts, bins = np.histogram(list_len_sentence, bins=10, range=(0, 150))
        print(f'{data} ->')
        print(f'counts :{counts}')
        print(f'bins : {bins}')
        print(f'max : {max(list_len_sentence)}')

        plt.hist(list_len_sentence, bins=100)
        # plt.axis([0, 140, 0, 250])
        # axis([xmin,xmax,ymin,ymax])
        plt.title(data)
        plt.ylabel('Counts')
        plt.xlabel('Length of sentence')
        plt.show()


main()


#### PLOT ####
