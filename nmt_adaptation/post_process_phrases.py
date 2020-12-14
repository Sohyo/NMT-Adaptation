from nmt_adaptation.util import arr2txt, text2arr
import random

def split_trg_src_phrase(path, save_name):
    """
    Split the phrase file into target and source
    :param path: where the phrase files are
    :param save_name: saving name. It will be added with '.de' and '.en'
    :return:
    """
    source = []
    target = []
    with open(path) as f:
        for line in f:
            arr_sents = line.split(' ||| ')
            source.append(arr_sents[0])
            target.append(arr_sents[1])

    arr2txt(source, "../data/edited_phrases/" + save_name + ".de")
    arr2txt(target, "../data/edited_phrases/" + save_name + ".en")


def edit_phrases(path, save_name, random_percentage):
    #TODO
    arr_phrase = text2arr(path)
    selected = random.choices(arr_phrase, k=len(arr_phrase)*random_percentage)


def add_tag(path, save_dir):
    tag_added_phrases = []
    phrases = text2arr(path)
    for line in phrases:
        tag_added_phrases.append("<PT> " + line + " </PT>")
    arr2txt(tag_added_phrases, save_dir)


def main():
    root_dir = "../data/extracted_phrases/"
    save_dir = "../data/edited_phrases/"
    data_names = ["EMEA", "GNOME", "JRC"]
    languages = ["de", "en"]
    # EMEA_path = "../data/extracted_phrases/EMEA_train_union"

    for data in data_names:
        split_trg_src_phrase(root_dir+data+"_train_union_4", data+"_train_phrase_4")
        for lang in languages:
            add_tag(f'{save_dir}{data}_train_phrase_4.{lang}', f'{save_dir}{data}_tagged_train_phrase_4.{lang}')


    # for data_name in data_names:
    #     split_trg_src_phrase(root_dir+data_name+"_train_union", data_name+"_train_phrase")



if __name__ == "__main__":
    main()
