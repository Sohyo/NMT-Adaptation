from nmt_adaptation.util import get_sorted_file_list_by_name, arr2txt, rm_dupl_from_list, text2arr
from nmt_adaptation.nmt_dev import NMT_dev
import re


def get_last_doc(arr_README_test):
    doc_numbers = []
    for line in arr_README_test:
        if re.sub("\D", "", line).isdigit():
            doc_numbers.append(re.sub("\D", "", line))
    return max(doc_numbers)


def get_dev_data(language, data_dir, save_dir, doc_list, n_data, name_data):
    sentences_arr = []
    doc_in_datasets = []
    sent_counts = 0
    last_doc = get_last_doc(text2arr(save_dir + "README_test"))
    new_doc_list = [doc for doc in doc_list if language in doc]
    for doc in new_doc_list[int(last_doc)+1:]:
        if language in doc:
            with open(data_dir + doc) as file:
                for sentence in file:
                    sentence = sentence.rstrip()
                    if sent_counts > n_data:
                        break
                    sent_counts += 1
                    sentences_arr.append(sentence)
                    doc_in_datasets.append(doc)
    write_readme(rm_dupl_from_list(doc_in_datasets), save_dir, name_data)
    arr2txt(sentences_arr, save_dir + ".".join(map(str, [name_data]+[language])))


def write_readme(doc_in_datasets, save_dir, name_data):
    with open(save_dir + "_".join(map(str, ["README"] + [name_data])), "+a") as txt_file:
        txt_file.write(
            "These are the documents used to make datasets :" + "\n\n\n")
        for line in doc_in_datasets:
            txt_file.write("".join(line) + "\n")
        txt_file.write("\n")


def main():
    # emea = NMT_dev(name="EMEA")
    # gnome = NMT_dev(name="GNOME")
    jrc = NMT_dev(name="JRC")

    # emea_doc_list = get_sorted_file_list_by_name(emea.data_dir)
    # gnome_doc_list = get_sorted_file_list_by_name(gnome.data_dir)
    jrc_doc_list = get_sorted_file_list_by_name(jrc.data_dir)
    # for language in [emea.src, emea.trg]:
    #     get_dev_data(language, emea.data_dir, emea.final_save_dir, doc_list=emea_doc_list,
    #                                    n_data=emea.n_dev, name_data="dev")
    # for language in [gnome.src, gnome.trg]:
    #     get_dev_data(language, gnome.data_dir, gnome.final_save_dir, doc_list=gnome_doc_list,
    #                                    n_data=gnome.n_dev, name_data="dev")
    for language in [jrc.src, jrc.trg]:
        get_dev_data(language, jrc.data_dir, jrc.final_save_dir, doc_list=jrc_doc_list,
                                       n_data=jrc.n_dev, name_data="dev")


if __name__ == "__main__":
    main()
