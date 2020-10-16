from util import get_sorted_file_list, arr2txt
from preprocess_datasets import split_into_src_trg


def get_src_trg_per_doc(root_dic, save_dir):
    xml_file_list = get_sorted_file_list(root_dic)
    for file in xml_file_list:
        src, trg = split_into_src_trg(root_dic + file)
        arr2txt(src, save_dir + file + ".de")
        arr2txt(trg, save_dir + file + ".en")


def main():
    # EMEA
    root_dir_EMEA = "/home/diego/PycharmProjects/my_fairseq/soyo/orig/EMEA_orig/xmlfiles_per_doc/"
    save_dir_EMEA = "/home/diego/Documents/thesis/NMT-Adaptation/data/custom_data/EMEA/"

    # GNOME
    root_dir_GNOME = "/home/diego/Documents/thesis/NMT-Adaptation/data/orig/GNOME/xmlfiles_per_doc/"
    save_dir_GNOME = "/home/diego/Documents/thesis/NMT-Adaptation/data/custom_data/GNOME/"

    # JRC
    root_dir_JRC = "/home/diego/Documents/thesis/NMT-Adaptation/data/orig/JRC/xmlfiles_per_doc/"
    save_dir_JRC = "/home/diego/Documents/thesis/NMT-Adaptation/data/custom_data/JRC/"

    # Run everything
    # get_src_trg_per_doc(root_dir_EMEA, save_dir_EMEA)
    get_sorted_file_list(root_dir_GNOME, save_dir_GNOME)
    # get_sorted_file_list(root_dir_JRC, save_dir_JRC)


if __name__ == "__main__":
    main()

