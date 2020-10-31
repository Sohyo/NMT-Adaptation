from util import get_sorted_file_list, text2arr
import xmltodict


'''
In this file, the alignment information file so-called xces file will be splited to several files which contain alignment info of only one document.
These files will be used to extract plain sentences from the xml files by OPUS tool.
'''


def split_xcesfile(root_dir):
    with open(root_dir+"/de-en.xml") as fd:
        orig_align_dict = xmltodict.parse(fd.read(), process_namespaces=True)
    if "GNOME" in root_dir:
        alignment_array = orig_align_dict['cesAlign']['linkList']
    else:
        alignment_array = orig_align_dict['cesAlign']['linkGrp']

    document_num = 0  # the splitted xces files will be counted from 0.
    for document in alignment_array:
        if not "GNOME" in root_dir:
            document = {'linkGrp': document}
        out = xmltodict.unparse(document, pretty=True)
        with open(root_dir+"/xces_files/" + str(document_num) + ".xml", 'a') as file:
            file.write(out)
        document_num += 1


def main():
    root_dir = "/home/diego/Documents/thesis/NMT-Adaptation/data/orig/"
    #datasets = ["EMEA", "GNOME", "JRC"]
    datasets = ["GNOME", "JRC"]
    for data in datasets:
        split_xcesfile(root_dir+data)


if __name__ == "__main__":
    main()