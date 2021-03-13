from nmt_adaptation.util import arr2txt, text2arr
import random
import os


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
        tag_added_phrases.append("<PT> " + line + "<\PT>")
    arr2txt(tag_added_phrases, save_dir)


class NMT_phrase:
    def __init__(self, root_dir="../data/extracted_phrases/",
                 save_dir="../data/edited_phrases/", languages=["de", "en"], name="EMEA"):
        self.root_dir = root_dir
        self.save_dir = save_dir
        self.languages = ["de", "en"]
        self.name = name

    def select_randomly(self, percentage):
        extracted_phrases = text2arr(os.path.join(self.root_dir, f'{self.name}_train_phrase_7'))
        selected_phrases = random.choices(extracted_phrases, k=int(len(extracted_phrases) * percentage))
        arr2txt(selected_phrases, os.path.join(self.root_dir, f'{self.name}_train_phrase_7_{percentage}'))


def main():
    emea = NMT_phrase(name="EMEA")
    gnome = NMT_phrase(name="GNOME")
    jrc = NMT_phrase(name="JRC")
    percentage = 0.5

    # emea.select_randomly(percentage)
    # gnome.select_randomly(percentage)
    # jrc.select_randomly(percentage)

    # Split the extracted phrases into src/trg
    # Then, put tag on the sentences
    # for data in [emea, gnome, jrc]:
    #     split_trg_src_phrase(path=os.path.join(data.root_dir, f'{data.name}_test_phrase_4_{percentage}'),
    #                          save_name=f'raw_{data.name}_train_phrase_7_{percentage}')
    #
    #     # Tagging every sentences
    #     for lang in data.languages:
    #         add_tag(path=f'{data.save_dir}raw_{data.name}_train_phrase_7_{percentage}.{lang}',
    #                 save_dir=f'{data.save_dir}{data.name}_tag_train_phrase_7_{percentage}.{lang}')
    #
    # For the anlaysis : without selected by percentage
    list_length = [6, 8, 10, 12, 14, 16, 18]
    for data in [emea, gnome, jrc]:
        for length in range(1, 21):
            split_trg_src_phrase(path=os.path.join(data.root_dir, f'{data.name}_test_phrase_{length}'),
                             save_name=f'raw_{data.name}_test_phrase_{length}')
            split_trg_src_phrase(path=os.path.join(data.root_dir, f'{data.name}_train_phrase_{length}'),
                             save_name=f'raw_{data.name}_train_phrase_{length}')


if __name__ == "__main__":
    main()
