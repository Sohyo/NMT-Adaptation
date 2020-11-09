from util import get_sorted_file_list


def create_arg_base(directory, download_dir, xces_files):
    default = "opus_read  --source de  --target en  --write_mode normal "
    arg_list = [default, "--directory", directory, "--download_dir", download_dir]
    base_bash_arg = " ".join(arg_list)

    bash_arg_list = []
    for xces in xces_files:
        command_line = [base_bash_arg, "--alignment_file", download_dir+"xmlfiles_per_doc/"+xces, "--write", xces[:-4]]
        bash_arg = " ".join(command_line)
        bash_arg_list.append(bash_arg)
    return bash_arg_list


def write_bash_script(bash_arg_list, file_name):
    with open(file_name, "w") as txt_file:
        for line in bash_arg_list:
            txt_file.write("".join(line) + "\n")


def generate_command_line(root_dir, directory):
    download_dir, alignment_file_dir = root_dir+directory+"/", root_dir+directory+"/xmlfiles_per_doc/"

    xces_files = get_sorted_file_list(download_dir+"xces_files")
    bash_arg_list = create_arg_base(directory, download_dir, xces_files)

    write_bash_script(bash_arg_list, root_dir+directory+"/run_cli_"+directory+".sh")


def main():
    root_dir = "/home/diego/Documents/thesis/NMT-Adaptation/data/orig/"
    datasets = ["EMEA_old", "GNOME", "JRC"]
    #datasets = ["GNOME", "JRC"]
    for data in datasets:
        generate_command_line(root_dir, data)


if __name__ == "__main__":
    main()