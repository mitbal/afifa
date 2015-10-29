# Perform one hot encoding
import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if len(sys.argv) < 3:
    print 'The usage is one_hot.py <input_file> <output_file>'
    sys.exit(0)

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')
dataset = []
symbols = set()

header = fin.readline().split(',')
num_features = len(header)-1
num_num = 0
labels = []

labels_numeric = ''
for line in fin.readlines():
    tokens = line[:-1].split(',')
    for token in tokens[:-1]:
        if not is_number(token) and token != '':
            symbols.add(token)
    labels.append(tokens[-1].rstrip())
    dataset.append(tokens[:-1])
fin.close()

row = dataset[1]
labels_numeric = ''
for (idx, col) in enumerate(row):
    if is_number(col):
        labels_numeric += header[idx]+','

symbols = list(symbols)
labels_symbols = ','.join(map(lambda x: 'c_'+x, symbols))
header = labels_numeric+labels_symbols+',class'
print header
fout.write(header+'\n')
for (nrow,row) in enumerate(dataset):
    sym_row = ['0']*len(symbols)
    num_row = ''
    for col in row:
        if is_number(col):
            num_row += col+','
        else:
            for (idx, sym) in enumerate(symbols):
                if sym == col:
                    sym_row[idx] = '1'
    prow = num_row+','.join(sym_row)+','+labels[nrow]
    print prow
    fout.write(prow +'\n')
fout.close()
