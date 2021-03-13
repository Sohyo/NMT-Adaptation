import os
from nmt_adaptation.util import arr2txt
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Exchange, remove, add tag.')
    parser.add_argument('--data_name', type=str,  default='EMEA',
                        help='The name of the datasets that we want to change the tag.')
    parser.add_argument('--new_data_name', type=str, default='1',
                        help='A new name of the file. This name will be combined with exited file and create new file name.')
    parser.add_argument('--new_tag', type=str, default='PT',
                        help='The new tag')

    args = parser.parse_args()
    return args.data_name, args.new_data_name, args.new_tag


def change_tag(root_dir, file_name, replacement_tag, new_file_name):

    """
    :param root_dir: The directory where the tagged phrases are
    :param file_name: The name of the tagged phrases file
    :param replacement_tag: The new tag wanted to change
    :param new_file_name: The new name of the file
    :return: Write the new data file
    """

    changed_dataset = []
    with open(os.path.join(root_dir, file_name)) as text:
        for sentence in text:

            # replace the tags located front and end of the sentences with the new tag!
            sentence = sentence.split()
            sentence[0] = f"{replacement_tag}"
            sentence[-1] = f"{replacement_tag}"
            # sentence[-1] = "PT"
            changed_dataset.append(' '.join(sentence))

    arr2txt(arr=changed_dataset, file_name=os.path.join(root_dir, new_file_name))


def remove_tags(root_dir, file_name):

    with open(os.path.join(root_dir, file_name)) as text:
        # This looks quite strange but it is basically split the very first and very last words from the sentences.
        # And then only take the middle string which is a sentence.
        data_tag_removed = [line.split(' ', 1)[1].rsplit(' ', 1)[0] for line in text]
    arr2txt(arr=data_tag_removed, file_name=os.path.join(root_dir, f'raw_{file_name}'))


def get_raw_dataset():
    # TODO
    pass


def add_tag():
    # TODO
    pass


def main():
    # TODO : maybe class can work better for this?
    root_dir = "../data/edited_phrases/"
    data_name, new_data_name, new_tag = parse_arguments()
    langs = [".de", ".en"]

    # EXCHANGE TAG
    for lang in langs:
        change_tag(root_dir=root_dir, file_name=f"{data_name}_tagged_train_phrase_4_0.5{lang}",
                   replacement_tag=new_tag, new_file_name=f"{data_name}_{new_data_name}_tag_train_phrase_4_0.5{lang}")

    # REMOVE tag
    # for lang in langs:
    #     remove_tags(root_dir=root_dir, file_name=f"{data_name}_tagged_train_phrase_4_0.5{lang}")

    # ADD TAG


if __name__ == '__main__':
    main()
