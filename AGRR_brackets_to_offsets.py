INPUT_FILE = 'D:/Gapping/dev_brackets.txt'
OUTPUT_FILE = 'D:/Gapping/dev.csv'
HEADER = 'text	class	cV	cR1	cR2	V	R1	R2'

LABELS = ['cV', 'cR1', 'cR2', 'V', 'R1', 'R2']
LABEL_TO_IDX = {}
for key in LABELS:
    LABEL_TO_IDX[key] = len(LABEL_TO_IDX) + 2

OPENING_MARKUP_ELEMENTS = [el + '[' for el in LABELS if el != 'V']
OPENING_TO_CLOSING = {}
for opening in OPENING_MARKUP_ELEMENTS:
    closing = opening[:-1] + ']'
    OPENING_TO_CLOSING[opening] = closing
EMPTY_ELEMENTS = ['V[]', 'V[ ]', 'V[  ]', 'cR1[]', 'cR2[]', 'R1[]', 'R2[]'] 
OPENING_MARKUP_ELEMENTS.extend(EMPTY_ELEMENTS)

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
            bracketed_markup = columns[1]
            current_idx = 0;
            to_print = [''] * (len(LABELS) + 2)
            to_print[1] = str(columns[0])
            to_continue = True
            offset = 0
            while to_continue:
                nearest_opening_idx = len(bracketed_markup) + 1
                nearest_opening = None
                for opening in OPENING_MARKUP_ELEMENTS:                 
                    found = bracketed_markup.find(opening, current_idx)
                    if found > -1 and found <= nearest_opening_idx:
                        nearest_opening_idx = found
                        nearest_opening = opening
                if nearest_opening is None:
                    to_continue = False
                elif nearest_opening in EMPTY_ELEMENTS:
                    to_print[0] += bracketed_markup[current_idx:nearest_opening_idx]
                    label = nearest_opening.split('[')[0]
                    if len(to_print[LABEL_TO_IDX[label]]) > 0:
                        to_print[LABEL_TO_IDX[label]] += ' '
                    to_print[LABEL_TO_IDX[label]] += str(nearest_opening_idx - offset) + ':' + str(nearest_opening_idx - offset)
                    current_idx = nearest_opening_idx + len(nearest_opening) + 1
                    offset += len(nearest_opening) + 1
                else:
                    closing = OPENING_TO_CLOSING[nearest_opening]
                    closing_idx = bracketed_markup.find(closing, nearest_opening_idx)
                    assert closing_idx != -1, line + 'No matching bracket for ' + nearest_opening
                    offset += len(nearest_opening)
                    beginning = nearest_opening_idx + len(nearest_opening)
                    ending = closing_idx - 1
                    to_print[0] += bracketed_markup[current_idx:nearest_opening_idx]
                    to_print[0] += bracketed_markup[beginning:ending]
                    label = closing[:-1]
                    if len(to_print[LABEL_TO_IDX[label]]) > 0:
                        to_print[LABEL_TO_IDX[label]] += ' '
                    to_print[LABEL_TO_IDX[label]] += str(beginning - offset) + ':' + str(ending - offset)
                    current_idx = closing_idx + len(closing)
                    offset += len(closing) + 1
                    
            to_print[0] += bracketed_markup[current_idx:]
            if len(columns) > 2 and len(columns[2]) > 0:
                to_print[0] = columns[2]
            print('\t'.join(to_print), file=f_out)