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


