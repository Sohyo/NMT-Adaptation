from nmt_adaptation.util import arr2txt
path = "../data/extracted_phrases/EMEA_train_union"

source = []
target = []
with open(path) as f:
    for line in f:
        arr_sents = line.split(' ||| ')
        source.append(arr_sents[0])
        target.append(arr_sents[1])

arr2txt(source, "../data/edited_phrases/EMEA_train_phrase.de")
arr2txt(target, "../data/edited_phrases/EMEA_train_phrase.en")


