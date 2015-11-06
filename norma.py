# Calulated mean and standard deviation from specified columns
import sys
import math

if len(sys.argv) < 4:
	print 'usage: <filename> <column_number> <norm_scale>'
	sys.exit(1)

filename = sys.argv[1]
cols = map(lambda x: int(x), sys.argv[2].split(','))
norm_file = sys.argv[3]

# Calculate average
count = 0
totalsum = [0]*len(cols)
fin = open(filename, 'r')
header = fin.readline()

for line in fin:
	tokens = line.split(',')
	for c in cols:
		totalsum[c] += float(tokens[c])
	count += 1
avg = map(lambda x: x/count, totalsum)

# Calculate standard deviation
stdev = [0]*len(cols)

fin.seek(0) 			# Go back to the beginning of the file
header = fin.readline()
for line in fin:
	tokens = line.split(',')
	for c in cols:
		stdev[c] += math.pow(float(tokens[c])-avg[c], 2)
std = map(lambda x: math.sqrt(x/count), stdev)

# Write mean and standard deviation to file
fout = open(norm_file, 'w')
fout.write('column,mean,std\n')
for c in cols:
	fout.write(','.join(map(lambda x: str(x), [c, avg[c], std[c]])))

fin.close()
fout.close()
