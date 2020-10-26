from nmt_adaptation.util import get_sorted_file_list


'''
    documents : 1 pdf file from OPUS 
    xces file : alignment information file
'''


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


def write_bash_script(bash_arg_list, file_name):
    with open(file_name, "w") as txt_file:
        for line in bash_arg_list:
            txt_file.write("".join(line) + "\n")


def generate_command_line(directory, download_dir, alignment_file_dir):
    xces_files = get_sorted_file_list(download_dir)
    base_bash_arg = create_arg_base(directory, download_dir)
    bash_arg_list = generate_bash_script_list(xces_files, base_bash_arg, alignment_file_dir)
    write_bash_script(bash_arg_list, "run_EMEA.sh")


def main():

    # EMEA
    directory_EMEA = 'EMEA'
    download_dir_EMEA = "/data/orig/EMEA/"
    alignment_file_dir_EMEA = "/data/orig/EMEA/xmlfiles_per_doc/"

    # GNOME
    directory_GNOME = 'GNOME'
    download_dir_GNOME = "/data/orig/GNOME/"
    alignment_file_dir_GNOME = "/data/orig/GNOME/xmlfiles_per_doc/"

    # JRC
    directory_JRC = 'JRC'
    download_dir_JRC = "/data/orig/JRC/"
    xces_files_JRC = "/home/diego/Documents/thesis/NMT-Adaptation/data/orig/JRC/xmlfiles_per_doc/"


    xces_files = get_sorted_file_list(download_dir_JRC)
    base_bash_arg = create_arg_base(download_dir_GNOME)
    bash_arg_list = generate_bash_script_list(xces_files, base_bash_arg, alignment_file_dir)
    generate_bash_script(bash_arg_list, "run_EMEA.sh")


if __name__ == "__main__":
    main()