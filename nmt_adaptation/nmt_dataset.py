from nmt_adaptation.util import arr2txt
from os.path import isfile, join

class NMT_dataset:
    def __init__(self, orig_dir="../data/orig_data/", name="EMEA",
                 src="de", trg="en", n_train=10000, n_valid=150, n_test=2000,
                 temp_dir="../data/temp_custom_data/",
                 new_dir="../data/temp_custom_data/",
                 final_save_dir="../data/custom_data/"):
        """
        :param orig_dir:
        :param src:
        :param trg:
        :param n_train:
        :param n_valid:
        :param n_test:
        """
        self.orig_dir = orig_dir
        self.src = src
        self.trg = trg
        self.n_train = n_train
        self.n_valid = n_valid
        self.n_test = n_test
        self.name = name
        self.temp_dir = join(temp_dir, name)
        self.new_dir = join(new_dir, name)
        self.save_dir = join(final_save_dir, name)

    @staticmethod
    def get_doc_name_list(self):
        german_docs_list = []
        english_docs_list = []
        with open(self.orig_dir) as f:
            for line in f:
                if '# de/' in line:
                    german_docs_list.append(line)
                elif '# en/' in line:
                    english_docs_list.append(line)
        return german_docs_list, english_docs_list

    def split_into_each_docs(self):

        """
        Split the results from OPUS tool into each docs.
        :param orig_root: directory where the result of OPUs tool
        :param name: name of the dataset
        """

        # This is counting of documents and at the same time it will bethe name of each files.
        doc_counts = 0
        with open(join(self.orig_dir, self.name + ".out")) as file:
            for line in file:

                # The file from OPUS tool starts a new file with "# de/".
                # Therefore, when the line is started with it, count number of documents.
                if line.startswith('# de/'):
                    doc_counts += 1

                doc_name = join(self.orig_dir, self.name, "xmlfiles_per_doc/", str(doc_counts))
                with open(doc_name, "+a") as file:
                    file.write("".join(line))

    # split the xml file into 2 plain text file(source/target)
    def split_into_src_trg(self, file_name):

        source, target = [], []
        src_text, trg_text = '', ''
        start_point = ">"

        with open(join(self.orig_dir, self.name, "xmlfiles_per_doc/" + file_name)) as f:
            for line in f:
                if line.startswith('(src)'):
                    if src_text == '':  # when it is the starting point of the sentence(or text)
                        src_text = line[line.index(start_point) + len(start_point):][:-1]
                    else:  # When there are several pieces of sentences, join them with blanks
                        src_text = ' '.join([src_text, line[line.index(start_point) + len(start_point):][:-1]])
                    # src_text += line[line.index(start_point) + len(start_point):][:-1]
                elif line.startswith('(trg)'):
                    if trg_text == '':  # when it is the starting point of the sentence(or text)
                        trg_text = line[line.index(start_point) + len(start_point):][:-1]
                    else:  # When there are several pieces of sentences, join them with blanks
                        trg_text = ' '.join([src_text, line[line.index(start_point) + len(start_point):][:-1]])
                elif line.startswith('==========='):  # finish saving the sentence as a block
                    source.append(src_text)
                    target.append(trg_text)
                    src_text = ''
                    trg_text = ''

        arr2txt(source[1:], join(self.temp_dir, file_name+".de"))
        arr2txt(target[1:], join(self.temp_dir, file_name+".en"))
