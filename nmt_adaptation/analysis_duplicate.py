from nmt_adaptation.util import text2arr, arr2txt
import os

"""
    This file analysis how many sentences are same/unique between 2 files.
        1. compare between trainset / testset - genuine one
        2. compare between fragmented trainset / testset - maximum 20 lenth for instance
"""


def compute_duplicate_orig_data(name_of_data):
    path = "./../data/custom_data"
    train = text2arr(os.path.join(path, name_of_data, "train.de"))
    test = text2arr(os.path.join(path, name_of_data, "test.de"))
    train = set(train)
    test = set(test)
    print(f'Duplicate of {name_of_data} : {len(train.intersection(test))}')


def compute_duplicate_from_phrase(name_of_data, phrase_length):
    path = "./../data/edited_phrases"
    train = text2arr(os.path.join(path, f"raw_{name_of_data}_train_phrase_{phrase_length}.de"))
    test = text2arr(os.path.join(path, f"raw_{name_of_data}_test_phrase_{phrase_length}.de"))
    train = filter_phrases(train, phrase_length)
    test = filter_phrases(test, phrase_length)
    train = set(train)
    test = set(test)
    print(f"{name_of_data}")
    print(f'trainset : {len(train)},testset : {len(test)}, Duplicate phrases : {len(train.intersection(test))}')
    print(f"proportion : {len(train.intersection(test))/ len(test)}")
    #print(f'Duplicate phrases : {len(train.intersection(test))}')


def filter_phrases(phrase_array, phrase_length):
    filtered_phrases = [phrase for phrase in phrase_array if len(phrase.split()) == phrase_length]
    return filtered_phrases


def main():
    # name_of_data = "GNOME"
    # datasets = ['EMEA', 'GNOME', 'JRC']
    # for data_name in datasets:
    #     compute_duplicate_orig_data(name_of_data=data_name)

    # Duplicate of phrases
    phrase_length = 1
    # print(f"Phrase length : {phrase_length}")
    # for data_name in datasets:
    #     compute_duplicate_from_phrase(name_of_data=data_name, phrase_length=phrase_length)

    # print(f"Phrase length : {phrase_length}")
    # for data_name in datasets:
    #     for phrase_length in range(1, 21):
    #         compute_duplicate_from_phrase(name_of_data=data_name, phrase_length=phrase_length)



    datasets = ['EMEA','GNOME', 'JRC']
    name_of_data = 'GNOME'
    phrase_length = 20
    path = "./../data/edited_phrases"
    train = text2arr(os.path.join(path, f"raw_{name_of_data}_train_phrase_{phrase_length}.de"))
    test = text2arr(os.path.join(path, f"raw_{name_of_data}_test_phrase_{phrase_length}.de"))

    print(name_of_data)
    amount_train = []
    amount_test = []
    amount_overlap = []
    for phrase_length in range(1, 21):
        train_list = [phrase for phrase in train if len(phrase.split()) == phrase_length]
        test_list = [phrase for phrase in test if len(phrase.split()) == phrase_length]
        train_list = set(train_list)
        test_list = set(test_list)
        amount_test.append(len(test_list))
        amount_train.append(len(train_list))
        amount_overlap.append(len(train_list.intersection(test_list)))
        # print(f"length of phrase : {phrase_length}")
        # print(f'trainset : {len(train_list)},testset : {len(test_list)}, Duplicate phrases : {len(train_list.intersection(test_list))}')
        # print(f"proportion : {len(train_list.intersection(test_list)) / len(test_list)}")

    print(amount_overlap)
    print("length of phrase: 1")
    print(f'testset : {amount_test[0]}, Duplicate phrases : {amount_overlap[0]}')
    print(f"proportion : {amount_overlap[0]/amount_test[0]}")

    print("length of phrase: 2")
    print(f'testset : {amount_test[1]}, Duplicate phrases : {amount_overlap[1]}')
    print(f"proportion : {amount_overlap[1] / amount_test[1]}")

    print("length of phrase: 3~4")
    print(f'testset : {amount_test[2]+amount_test[3]}, Duplicate phrases : {amount_overlap[2]+amount_overlap[3]}')
    print(f"proportion : {(amount_overlap[2]+amount_overlap[3]) / (amount_test[2]+amount_test[3])}")

    print("length of phrase: 5~7")
    print(f'testset : {sum(amount_test[4:7])}, Duplicate phrases : {sum(amount_overlap[4:7])}')
    print(f"proportion : {sum(amount_overlap[4:7])/ sum(amount_test[4:7])}")

    print("length of phrase: 8~12")
    print(f'testset : {sum(amount_test[7:12])}, Duplicate phrases : {sum(amount_overlap[7:12])}')
    print(f"proportion : {sum(amount_overlap[7:13]) / sum(amount_test[7:13])}")

    print("length of phrase: 13~20")
    print(f'testset : {sum(amount_test[12:20])}, Duplicate phrases : {sum(amount_overlap[12:20])}')
    print(f"proportion : {sum(amount_overlap[12:20]) /sum(amount_test[12:20])}")

main()
