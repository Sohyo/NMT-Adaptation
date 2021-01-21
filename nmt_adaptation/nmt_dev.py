from os.path import join

class NMT_dev:
    def __init__(self, name="EMEA",
                 src="de", trg="en", n_dev=2000,
                 data_dir="../data/temp_custom_data/",
                 final_save_dir="../data/custom_data/"):
        """
        :param name:
        :param src:
        :param trg:
        :param n_dev:
        :param data_dir:
        :param final_save_dir:
        """
        self.src = src
        self.trg = trg
        self.n_dev = n_dev
        self.name = name
        self.data_dir = join(data_dir, name)
        self.final_save_dir = join(final_save_dir, name)
