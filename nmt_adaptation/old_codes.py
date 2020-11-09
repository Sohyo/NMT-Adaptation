import numpy as np


# EMEA_old path
emea_de_path = "temp_custom_data/EMEA_old/EMEA_old.de-en.de"
emea_en_path = "temp_custom_data/EMEA_old/EMEA_old.de-en.en"

# EMEA_old arrs - de, en
arr_emea_de = text2arr(emea_de_path)
arr_emea_en = text2arr(emea_en_path)
# print(arr_emea_en[:10])
join = np.column_stack((arr_emea_de[:10], arr_emea_en[:10]))
print(join[0][0])



# split arrs into train, valid and test sets
'''
train_de, valid_de, test_de = split_arr(arr_emea_de, 10000, 1000, 2000)
train_en, valid_en, test_en = split_arr(arr_emea_en, 10000, 1000, 2000)

#write to txt files!
names_de = ["train.de", "valid.de", "test.de"]
names_en = ["train.en", "valid.en", "test.en"]
langs = ["de", "en"]
sets = ["train", "valid", "test"]

arr2txt(train_de, "train.de")
arr2txt(valid_de, "valid.de")
arr2txt(test_de, "test.de")

arr2txt(train_en, "train.en")
arr2txt(valid_en, "valid.en")
arr2txt(test_en, "test.en")
'''



def gen_datasets_array(data_dir, num_data_splits, language):
    xml_file_list = get_sorted_file_list(data_dir)
    doc_dict = {}
    for file in xml_file_list:
        if language in file:
            doc_dict["language"] = language
            # doc_arr.append(text2arr(data_dir + file))
     # train, valid, test = gen_train_val_test(doc_arr, num_data_splits)
    #data_array = [train, valid, test]
    #return data_array


def gen_train_val_test(doc_arr, num_data_splits):
    sentences_arr = []
    sent_counts = 0
    doc_counts = 0
    for doc in doc_arr:

        for sentence in doc:
            if sent_counts > sum(num_data_splits.values()):
                break

            sentences_arr.append(sentence)
            sent_counts += 1
        doc_counts += 1
    train, valid, test = sentences_arr[:num_data_splits["n_train"]], \
                         sentences_arr[num_data_splits["n_train"]:num_data_splits["n_train"] + num_data_splits["n_valid"]], \
                         sentences_arr[-num_data_splits["n_test"]:]

    return train, valid, test


def write_train_val_test(data_dir, name_dataset, dict_datasets,  language):
    for data in dict_datasets:
        name = ".".join(map(str, [name_dataset] + [data] + [language]))  # ex) EMEA_old.train.en
        print(data_dir+name)
        arr2txt(dict_datasets[data], data_dir+name)
        #dict_datasets[data]
    # for dataset, name_split in data_array, name_splits:
    #     print(name_split)
    #     name = ".".join(map(str, [name_dataset] + [name_split] + [language]))   # ex) EMEA_old.train.en
    #     print(name)
    #     arr2txt(dataset, data_dir+name)