from util import get_sorted_file_list, arr2txt
from func_for_pre_post_process import split_into_src_trg


def main():
    root_dir_EMEA = "/home/diego/Documents/thesis/NMT-Adaptation/data/orig/EMEA/xmlfiles_per_doc/"
    save_dir = "/data/temp_custom_data/EMEA_old/"

    xml_file_list = get_sorted_file_list(root_dir_EMEA)
    for file in xml_file_list:
        src, trg = split_into_src_trg(root_dir_EMEA+file)
        arr2txt(src, save_dir + file + ".de")
        arr2txt(trg, save_dir + file + ".en")


if __name__ == "__main__":
    main()

