# Perform evaluation by comparing ground truth labels and prediction
# such as accuracy, confusion matrix, etc

import sys

f1 = open('../payment/labels', 'r')
f2 = open('../payment/prediction', 'r')

label = []
prediction = []
conf_matrix = [[0]*4 for x in xrange(4)]

for line1 in f1.readlines():
	line2 = f2.readline()
	i = int(float(line1[:-1]))-1
	j = int(float(line2[:-1]))-1
	conf_matrix[i][j] += 1

print(' '.join(map(lambda x: str(x), range(1,5))))
for i in xrange(4):
	row = str(i+1)+' '
	for j in xrange(4):
		row += str(conf_matrix[i][j]) +' '
	print row

# Calculate accuracy
acc = 0
total = 0
for i in xrange(4):
	for j in xrange(4):
		if i==j:
			acc += conf_matrix[i][j]
		total += conf_matrix[i][j]

print 'acc', (float(acc)/total)*100
