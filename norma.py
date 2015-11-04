# Normalize single colum
import sys
import math

if len(sys.argv) < 3:
	print 'usage: <filename> <column_number>'
	sys.exit(1)

filename = sys.argv[1]
numcol = sys.argv[2]
fin = open(filename, 'r')

dataset = []
totalsum = 0
count = 0
for line in fin.readlines():
	tokens = line.split(',')
	dataset.append(tokens)

	for idx, token in enumerate(tokens):
		if idx == numcol:
			totalsum += float(token)
			count += 1
avg = totalsum / count
stdev = 0

for row in dataset:
	for idx, col in enumerate(row):
		if idx == numcol:
			stdev += math.pow((col-avg), 2)
stdev = math.sqrt(stdev/count)

for row in dataset:
	for idx, col in enumerate(row):
		if idx == numcol:
			row[idx] = row[idx]/stdev

fout = open(filename, 'w')
for row in dataset:
	fout.write(','.join(row))
