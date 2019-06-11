INPUT_FILE = 'D:/Gapping/dev.csv'
OUTPUT_FILE = 'D:/Gapping/dev_brackets.txt'
IDX_TO_LABEL = {0:'cV', 1:'cR1', 2:'cR2', 3:'V', 4:'R1', 5:'R2'}
HEADER = 'class	mark_up'
print_header = True

with open(INPUT_FILE, 'r', encoding='utf-8') as f_in:
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
        if print_header:
            print(HEADER, file=f_out)
        header = True
        for line in f_in:
            if header:
                header = False
                continue
            columns = line.strip().split('\t')
            if columns[1] == '1':
                text = columns[0]
                gapping = []
                for i, el in enumerate(columns[2:]):
                    if el != '':
                        offsets = el.split(' ')
                        for offset in offsets:
                            beg = int(offset.split(':')[0])
                            end = int(offset.split(':')[1])
                            gapping.append([beg, end, IDX_TO_LABEL[i]])
                gapping = sorted(gapping)
                assert len(gapping) > 0, "No coord"
                previous_idx = 0
                to_print = columns[1] + '\t'
                for gap in gapping:
                    to_print += text[previous_idx:gap[0]]
                    to_print += gap[2] + '['
                    to_print += text[gap[0]:gap[1]]
                    if gap[2] == 'V':
                        to_print += ']' + ' '
                    else:
                        to_print += ' ' + gap[2] + ']'
                    previous_idx = gap[1]
                to_print += text[previous_idx:]
                print(to_print, file=f_out)
            else:
                print(columns[1] + '\t' + columns[0], file=f_out)
            