#!/usr/bin/env python

# Apply normalization using pre-calculated mean and stdev
import sys

if len(sys.argv) < 3:
    print 'usage: <input_file> <output_file> <scale_file>'

input_file = sys.argv[1]
output_file = sys.argv[2]
scale_file = sys.argv[2]

fin = open(input_file, 'r')
fnorm = open(scale_file, 'r')
fout = open(output_file, 'w')

norms = []
header = fnorm.readline()
for line in fnorm:
    tokens = line.split(',')
    norms.append([int(tokens[0]), float(tokens[1]), float(tokens[2])])

header = fin.readline()
fout.write(header)
for line in fin:
    tokens = line.split(',')
    for norm in norms:
        idx = norm[0]
        if norm[2] > 1e-10:
            tokens[idx] = str((float(tokens[idx])-norm[1]) / norm[2])
        else:
            tokens[idx] = str((float(tokens[idx])-norm[1]))
    fout.write(','.join(tokens))

fin.close()
fnorm.close()
fout.close()
