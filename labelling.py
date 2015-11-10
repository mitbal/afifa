# Play around with class labels

import sys

if len(sys.argv) < 4:
    print 'usage: <input_file> <output_file> <label_file>'
    sys.exit(1)

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')
flabel = open(sys.argv[3], 'r')

groups = {}

# Load labels file
for line in flabel:
    tokens = line.rstrip().split(' ')
    label = tokens[0]
    groups[label] = tokens[1].split(',')

# Read per line
header = fin.readline()
fout.write(header)
for line in fin:
    tokens = line.split(',')
    former_label = tokens[-1].rstrip()
    label = ''
    for key in groups.keys():
        if former_label in groups[key]:
            label = key
            break
    if label != '':
        fout.write(','.join(tokens[:-1])+','+label+'\n')

fin.close()
fout.close()
flabel.close()
