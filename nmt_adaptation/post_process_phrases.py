from nmt_adaptation.util import arr2txt


def split_trg_src_phrase(path, save_name):
    source = []
    target = []
    with open(path) as f:
        for line in f:
            arr_sents = line.split(' ||| ')
            source.append(arr_sents[0])
            target.append(arr_sents[1])

    arr2txt(source, "../data/edited_phrases/" + save_name + ".de")
    arr2txt(target, "../data/edited_phrases/" + save_name + ".en")


def main():
    root_dir = "../data/extracted_phrases/"
    data_names = ["EMEA", "GNOME", "JRC"]
    EMEA_path = "../data/extracted_phrases/EMEA_train_union"

    for data_name in data_names:
        split_trg_src_phrase(root_dir+data_name+"_train_union", data_name+"_train_phrase")


if __name__ == "__main__":
    main()
