import sys
import csv
import xmltodict
csv.field_size_limit(sys.maxsize)

'''
    Preprocess dataset to get ready to feed it into the model. (train/valid/test/)
    
    1. Using 'OPUS Tool' to get the aligned plain textual datasets.
        1) The information of alignment is in the xces file from OPUS. In order to split the plain texts per documents,
        xces file is needed to be splitted per documents. 
        2) Generate command lines for using OPUS tool. -> Run it!
        3) Based on the splitted xces files, the aligned plain text can be extracted. However, still this need to be divided into source and target languages.
         
    2. Make the proper training/validation/test datasets.
        1) Read several text files and generate textfiles of each languages. 
        2) 
    
'''


# Read the xces file(xml) into dictionary
def xml2dict(xml_path):
    with open(xml_path) as fd:
        orig_align_dict = xmltodict.parse(fd.read())
    return orig_align_dict


# divide dictionary of the xces file into xml files per doc
def split_dict2xml(xml_path, xces_save_dir):
    with open(xml_path) as fd:
        orig_align_dict = xmltodict.parse(fd.read(), process_namespaces=True)

    document_num = 0  # the splitted xces files will be counted from 0.

    for document in orig_align_dict['cesAlign']['linkGrp']:
        document = {'linkGrp': document}
        out = xmltodict.unparse(document, pretty=True)
        with open(xces_save_dir + str(document_num) + ".xml", 'a') as file:
            file.write(out)
        document_num += 1


# split the xml file into 2 plain text file(source/target)
def split_into_src_trg(text_path):

    source, target = [], []
    src_text, trg_text = '', ''
    start_point = ">"

    with open(text_path) as f:
        for line in f:
            if line.startswith('(src)'):
                if src_text == '':  # when it is the starting point of the sentence(or text)
                    src_text = line[line.index(start_point) + len(start_point):][:-1]
                else:   # When there are several pieces of sentences, join them with blanks
                    src_text = ' '.join([src_text, line[line.index(start_point) + len(start_point):][:-1]])
                # src_text += line[line.index(start_point) + len(start_point):][:-1]
            elif line.startswith('(trg)'):
                if trg_text == '':  # when it is the starting point of the sentence(or text)
                    trg_text = line[line.index(start_point) + len(start_point):][:-1]
                else:   # When there are several pieces of sentences, join them with blanks
                    trg_text = ' '.join([src_text, line[line.index(start_point) + len(start_point):][:-1]])
            elif line.startswith('==========='):    # finish saving the sentence as a block
                source.append(src_text)
                target.append(trg_text)
                src_text = ''
                trg_text = ''
    return source[1:], target[1:]


# get train, validation and test datasets with given number of sentences.
def split_datasets(arr, n_train, n_valid, n_test):
    total_num = len(arr)
    if n_train+n_valid+n_test <= total_num:
        train_set, valid_set, test_set = arr[:n_train], arr[n_train:n_valid+n_train], \
                                         arr[n_valid+n_train:n_valid+n_train+n_test]
    return train_set, valid_set, test_set


def format_filename(lang, sets):
    return ".".join(map(str, [sets] + [lang]))

