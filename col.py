# Damn, multiple libraries using different label for classes
# Increment or decrement the class label by 1

import sys

if len(sys.argv) < 5:
	print 'Usage python col.py <input_file> <output_file> <label_column> <value>'
	sys.exit(1)

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')
class_col = int(sys.argv[3])
inc = int(sys.argv[4])

for line in fin.readlines():
	tokens = line.split(' ')
	row = str(int(tokens[class_col])+inc)+' ' +' '.join(tokens[1:])
	fout.write(row)

print 'done'
