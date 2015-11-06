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
fheader = open('header.txt', 'w')
dataset = []
symbols = set()

header = fin.readline().split(',')
num_features = len(header)-1
num_num = 0
labels = []

labels_numeric = ''
for line in fin.readlines():
    tokens = line[:-1].split(',')
    for (ncol,token) in enumerate(tokens[:-1]):
        if not is_number(token) and token != '':
            symbols.add(header[ncol]+'_'+token)
    labels.append(tokens[-1].rstrip())
    dataset.append(tokens[:-1])
fin.close()

row = dataset[1]
labels_numeric = ''
for (idx, col) in enumerate(row):
    if is_number(col):
        labels_numeric += header[idx]+','

symbols = sorted(list(symbols))
labels_symbols = ','.join(map(lambda x: 'c_'+x, symbols))
outheader = labels_numeric+labels_symbols+',class'
print outheader
fheader.write(outheader+'\n')
fheader.close()
fout.write(outheader+'\n')
for (nrow,row) in enumerate(dataset):
    sym_row = ['0']*len(symbols)
    num_row = ''
    for (ncol,col) in enumerate(row):
        if is_number(col):
            num_row += col+','
        else:
            for (idx, sym) in enumerate(symbols):
                #print sym, header[ncol]+'_'+col
                if sym == header[ncol]+'_'+col:
                    sym_row[idx] = '1'
    prow = num_row+','.join(sym_row)+','+labels[nrow]
    if nrow % 10000 == 0:
        # print prow
        print str(nrow)+'/'+str(len(dataset))
    fout.write(prow +'\n')
fout.close()
