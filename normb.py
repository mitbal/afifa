#!/usr/bin/env python

# Apply normalization using pre-calculated mean and stdev
import sys

if len(sys.argv) < 3:
	print 'usage: <filename> <norm_file>'

filename = sys.argv[1]
norm_file = sys.argv[2]

fin = open(filename, 'r')
fnorm = open(norm_file, 'r')
fout = open(filename+'_n', 'w')

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
