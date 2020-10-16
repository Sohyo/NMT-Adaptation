# EMEA path
emea_de_path = "custom_data/EMEA/EMEA.de-en.de"
emea_en_path = "custom_data/EMEA/EMEA.de-en.en"

# EMEA arrs - de, en
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