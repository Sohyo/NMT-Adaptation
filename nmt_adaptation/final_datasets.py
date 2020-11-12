from util import get_sorted_file_list_by_name, arr2txt, rm_dupl_from_list, cleanup_datasets
from preprocess import NMT_dataset


def get_dataset(language, temp_dir, save_dir, doc_list, doc_in_datasets, n_data, name_data):
    sentences_arr = []
    temp_doc_in_datasets = []
    sent_counts = 0
    doc_list = [doc for doc in doc_list if doc not in doc_in_datasets]

    for doc in doc_list:
        if language in doc:
            with open(temp_dir + doc) as file:
                for sentence in file:
                    sentence = sentence.rstrip()
                    if sent_counts > n_data:
                        break
                    sent_counts += 1
                    sentences_arr.append(sentence)
                    temp_doc_in_datasets.append(doc)
                    doc_in_datasets.append(doc)
    write_readme(rm_dupl_from_list(temp_doc_in_datasets), save_dir, name_data)
    arr2txt(sentences_arr, save_dir + ".".join(map(str, [name_data] + [language])))
    return rm_dupl_from_list(doc_in_datasets)


def write_readme(doc_in_datasets, save_dir, name_data):
    with open(save_dir + "_".join(map(str, ["README"] + [name_data])), "+a") as txt_file:
        txt_file.write(
            "These are the documents used to make datasets :" + "\n\n\n")
        for line in doc_in_datasets:
            txt_file.write("".join(line) + "\n")
        txt_file.write("\n")


def main():
    emea = NMT_dataset(name="EMEA")
    gnome = NMT_dataset(name="GNOME")
    jrc = NMT_dataset(name="JRC")

    # emea.split_into_each_docs(emea.orig_dir)
    # gnome.split_into_each_docs(gnome.orig_dir)
    # jrc.split_into_each_docs(jrc.orig_dir)
    #
    # emea_files = get_sorted_file_list_by_name(emea.orig_dir+"xmlfiles_per_doc/")
    # for file in emea_files:
    #     emea.split_into_src_trg(emea.orig_dir, file, emea.temp_dir)
    #
    # gnome_files = get_sorted_file_list_by_name(gnome.orig_dir + "xmlfiles_per_doc/")
    # for file in gnome_files:
    #     gnome.split_into_src_trg(gnome.orig_dir, file, gnome.temp_dir)
    #
    # jrc_files = get_sorted_file_list_by_name(jrc.orig_dir + "xmlfiles_per_doc/")
    # for file in jrc_files:
    #     jrc.split_into_src_trg(jrc.orig_dir, file, jrc.temp_dir)

    cleanup_datasets(emea.temp_dir, emea.new_dir)
    cleanup_datasets(gnome.temp_dir, gnome.new_dir)
    cleanup_datasets(jrc.temp_dir, jrc.new_dir)

    emea_doc_list = get_sorted_file_list_by_name(emea.new_dir)
    gnome_doc_list = get_sorted_file_list_by_name(gnome.new_dir)
    jrc_doc_list = get_sorted_file_list_by_name(jrc.new_dir)

    for language in [jrc.src, jrc.trg]:
        doc_in_datasets = []
        doc_in_datasets = get_dataset(language, jrc.new_dir, jrc.save_dir, doc_list=jrc_doc_list, doc_in_datasets=doc_in_datasets,
                                      n_data=jrc.n_train, name_data="train")
        doc_in_datasets = get_dataset(language, jrc.new_dir, jrc.save_dir, doc_list=jrc_doc_list,
                                      doc_in_datasets=doc_in_datasets, n_data=jrc.n_valid, name_data="valid")
        get_dataset(language, jrc.new_dir, jrc.save_dir, doc_list=jrc_doc_list, doc_in_datasets=doc_in_datasets,
                    n_data=jrc.n_test,name_data="test")

    for language in [emea.src, emea.trg]:
        doc_in_datasets = []
        doc_in_datasets = get_dataset(language, emea.new_dir, emea.save_dir, doc_list=emea_doc_list,
                                      doc_in_datasets=doc_in_datasets,
                                      n_data=emea.n_train, name_data="train")
        doc_in_datasets = get_dataset(language, emea.new_dir, emea.save_dir, doc_list=emea_doc_list,
                                      doc_in_datasets=doc_in_datasets, n_data=emea.n_valid, name_data="valid")
        get_dataset(language, emea.new_dir, emea.save_dir, doc_list=emea_doc_list, doc_in_datasets=doc_in_datasets,
                    n_data=emea.n_test, name_data="test")

    for language in [gnome.src, gnome.trg]:
        doc_in_datasets = []
        doc_in_datasets = get_dataset(language, gnome.new_dir, gnome.save_dir, doc_list=gnome_doc_list,
                                      doc_in_datasets=doc_in_datasets,
                                      n_data=gnome.n_train, name_data="train")
        doc_in_datasets = get_dataset(language, gnome.new_dir, gnome.save_dir, doc_list=gnome_doc_list,
                                      doc_in_datasets=doc_in_datasets, n_data=gnome.n_valid, name_data="valid")
        get_dataset(language, gnome.new_dir, gnome.save_dir, doc_list=gnome_doc_list,
                    doc_in_datasets=doc_in_datasets,
                    n_data=gnome.n_test, name_data="test")


if __name__ == "__main__":
    main()
