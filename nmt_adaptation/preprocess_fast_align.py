from nmt_adaptation.util import text2arr


def write_fast_align_input(array_de, array_en, save_directory, data):
    for line_num in range(len(array_de)):
        with open(save_directory+"_".join(map(str, ["fastalign"]+[data])), "+a") as txt_file:
            if (array_de[line_num] and array_en[line_num]) is not "":
                txt_file.write(" ||| ".join(map(str, [array_de[line_num]] + [array_en[line_num]])) + "\n")


def main():
    root_dir = "/home/diego/Documents/thesis/NMT-Adaptation/data/custom_data/"
    data_name_list = ["EMEA", "GNOME", "JRC"]
    dataset = ["train", "valid", "test"]
    languages = ["de", "en"]
    arr_en = []
    arr_de = []
    for data_name in data_name_list:
        directory = root_dir+data_name+"/"
        for data in dataset:
            arr_de = text2arr(directory+".".join(map(str, [data] + ["de"])))
            arr_en = text2arr(directory+".".join(map(str, [data] + ["en"])))
            write_fast_align_input(arr_de, arr_en, directory, data)


if __name__ == "__main__":
    main()
