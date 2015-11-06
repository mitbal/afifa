#!/usr/bin/env python

# Apply one hot encoding into new file
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

import sys
if len(sys.argv) < 5:
    print 'usage: <input_file> <output_file> <header_file> <mode>'
    sys.exit(1)

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')
fheader = open(sys.argv[3], 'r')
mode = sys.argv[4]

outheader = fheader.readline()
num_symbols = int(fheader.readline())
symbols = outheader.split(',')[-(num_symbols+1):-1]
fout.write(outheader)
ori_header = fin.readline().split(',')
nrow = 0
for line in fin:
    tokens = line.split(',')
    row = tokens[:-1]
    nrow += 1
    sym_row = ['0']*len(symbols)
    num_row = ''
    for (ncol,col) in enumerate(row):
        if is_number(col):
            num_row += col+','
        else:
            for (idx, sym) in enumerate(symbols):
                if sym == 'c_'+ori_header[ncol]+'_'+col:
                    sym_row[idx] = '1'
    prow = num_row+','.join(sym_row)+','+tokens[-1]
    if nrow % 10000 == 0:
        print str(nrow)+' row(s)...'
    fout.write(prow)

fin.close()
fheader.close()
fout.close()
