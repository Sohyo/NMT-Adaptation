from os import walk, listdir
from os.path import isfile, join
from util import get_sorted_file_list


'''
    documents : 1 pdf file from OPUS 
    xces file : alignment information file
'''
#TODO : clean up code and maybe need to think about how I can reuse this for the other datasets

def create_arg_base(directory, download_dir):
    default = "opus_read  --source de  --target en  --write_mode normal "
    arg_list = [default, "--directory", directory, "--alignment_file", "--download_dir", download_dir]
    base_bash_arg = " ".join(arg_list)
    return base_bash_arg


def generate_bash_script_list(base_bash_arg, xces_files, alignment_file_dir):
    bash_arg_list = []
    for xces in xces_files:
        command_line = [base_bash_arg, alignment_file_dir + xces, "--write", xces[:-4]]
        bash_arg = " ".join(command_line)
        bash_arg_list.append(bash_arg)
    return bash_arg_list


def generate_bash_script(bash_arg_list, file_name):
    with open(file_name, "w") as txt_file:
        for line in bash_arg_list:
            txt_file.write("".join(line) + "\n")


xces_files_dir = '/home/diego/PycharmProjects/my_fairseq/soyo/orig/EMEA_orig/xces_files/'
save_dir = '/home/diego/PycharmProjects/my_fairseq/soyo/orig/EMEA_orig/xmlfiles_per_doc/'
alignment_file_dir = "/home/diego/PycharmProjects/my_fairseq/soyo/orig/EMEA_orig/xces_files/"
directory = 'EMEA'
download_dir = "/home/diego/PycharmProjects/my_fairseq/soyo/orig/EMEA_orig/"

xces_files = get_sorted_file_list(xces_files_dir)
base_bash_arg = create_arg_base(directory)
print(base_bash_arg)
bash_arg_list = generate_bash_script_list(xces_files, base_bash_arg, alignment_file_dir)
generate_bash_script(bash_arg_list, "run_EMEA.sh")

