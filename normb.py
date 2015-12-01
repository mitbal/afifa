#!/usr/bin/env python

# Apply normalization using pre-calculated mean and stdev
import sys
import math

if len(sys.argv) < 3:
    print 'usage: <input_file> <output_file> <scale_file>'

input_file = sys.argv[1]
output_file = sys.argv[2]
scale_file = sys.argv[3]

fin = open(input_file, 'r')
fnorm = open(scale_file, 'r')
fout = open(output_file, 'w')

norms = []
header = fnorm.readline()
for line in fnorm:
    tokens = line.split(',')
    mean = float(tokens[1])
    std = float(tokens[2])
    if not (math.isnan(mean) or math.isnan(std) or mean < 1e-10 or std < 1e-10):
        norms.append([int(tokens[0]), float(tokens[1]), float(tokens[2])])

header = fin.readline()
fout.write(header)
for line in fin:
    tokens = line.split(',')
    for norm in norms:
        idx = norm[0]
        tokens[idx] = str((float(tokens[idx])-norm[1]) / norm[2])
    fout.write(','.join(tokens))

fin.close()
fnorm.close()
fout.close()
