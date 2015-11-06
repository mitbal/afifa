# Get header of features after one hot encoding

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

import sys

if len(sys.argv) < 3:
    print 'usage: <input_file> <output_file>'

fin = open(sys.argv[1], 'r')
fheader = open('header.txt', 'w')
symbols = set()

header = fin.readline().split(',')
num_features = len(header)-1
labels = []

row = []
for line in fin.readlines():
    tokens = line[:-1].split(',')
    for (ncol, token) in enumerate(tokens[:-1]):
        if not is_number(token) and token != '':
            symbols.add(header[ncol]+'_'+token)
    labels.append(tokens[-1].rstrip())
    row = tokens[:-1]
fin.close()

labels_numeric = ''
for (idx, col) in enumerate(row):
    if is_number(col):
        labels_numeric += header[idx]+','

symbols = sorted(list(symbols))
labels_symbols = ','.join(['c_'+x for x in symbols])
outheader = labels_numeric+labels_symbols+',class'
print outheader
fheader.write(outheader+'\n')
fheader.close()
