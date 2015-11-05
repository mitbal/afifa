# Calulated mean and standard deviation from specified columns
import sys
import math

if len(sys.argv) < 4:
	print 'usage: <filename> <column_number> <norm_scale>'
	sys.exit(1)

filename = sys.argv[1]
cols = map(lambda x: int(x), sys.argv[2].split(','))
norm_file = sys.argv[3]

dataset = []
totalsum = [0]*len(cols)
count = 0

# Read input and count average
fin = open(filename, 'r')
header = fin.readline()
for line in fin:
	tokens = line.split(',')
	dataset.append(tokens)
	for c in cols:
		totalsum[c] += float(tokens[c])
	count += 1
avg = map(lambda x: x/count, totalsum)

# Count standard deviation
stdev = [0]*len(cols)
for row in dataset:
	for c in cols:
		stdev[c] += math.pow(float(row[c])-avg[c], 2)
std = map(lambda x: math.sqrt(x/count), stdev)

# Write mean and standard deviation to file
fout = open()
fout.write('column,mean,std\n')
for c in cols:
	fout.write(str(c)+','+avg[c]+','std[c])

fin.close()
fout.close()
