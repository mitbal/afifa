#!/usr/bin/env python

# Calulated mean and standard deviation from specified columns
import sys
import math

if len(sys.argv) < 4:
	print 'usage: <input_file> <scale_file> <column_numbers>'
	sys.exit(1)

input_file = sys.argv[1]
scale_file = sys.argv[2]
columns = sys.argv[3].split(',')

# parse column number
cols = []
for col in columns:
	cs = col.split('-')
	if len(cs) == 2:
		cols += range(int(cs[0]), int(cs[1])+1)
	else:
		cols += [int(cs[0])]

# Calculate average
count = 0
totalsum = {}
fin = open(input_file, 'r')
header = fin.readline()

for line in fin:
	tokens = line.split(',')
	for c in cols:
		if not c in totalsum:
			totalsum[c] = 0
		totalsum[c] += float(tokens[c])
	count += 1
avg = {}
for c in totalsum:
	avg[c] = totalsum[c] / float(count)

# Calculate standard deviation
stdev = {}
fin.seek(0) 			# Go back to the beginning of the file
header = fin.readline()
for line in fin:
	tokens = line.split(',')
	for c in cols:
		if not c in stdev:
			stdev[c] = 0
		stdev[c] += math.pow(float(tokens[c])-avg[c], 2)
std = {}
for c in stdev:
	std[c] = math.sqrt(stdev[c]/count)

# Write mean and standard deviation to file
fout = open(scale_file, 'w')
fout.write('column,mean,std\n')
for c in cols:
	fout.write(','.join(map(lambda x: str(x), [c, avg[c], std[c]]))+'\n')

fin.close()
fout.close()
