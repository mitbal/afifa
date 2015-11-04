# Normalize single colum
import sys
import math

if len(sys.argv) < 3:
	print 'usage: <filename> <column_number>'
	sys.exit(1)

filename = sys.argv[1]
numcol = int(sys.argv[2])
fin = open(filename, 'r')

dataset = []
totalsum = 0
count = 0
header = fin.readline()
for line in fin:
	tokens = line.split(',')
	dataset.append(tokens)
	totalsum += float(tokens[numcol])
	count += 1
avg = totalsum / count
stdev = 0

for row in dataset:
	for idx, col in enumerate(row):
		if idx == numcol:
			stdev += math.pow((int(col)-avg), 2)
stdev = math.sqrt(stdev/count)

for row in dataset:
	for idx, col in enumerate(row):
		if idx == numcol:
			row[idx] = float(row[idx])/stdev

fout = open('normed_'+filename, 'w')
fout.write(header)
for row in dataset:
	fout.write(','.join(map(lambda x: str(x), row)))

fin.close()
fout.close()
print 'mean', avg
print 'std', stdev
print 'selesai'
