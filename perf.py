#!/usr/bin/env python

# Perform evaluation by comparing ground truth labels and prediction
# such as accuracy, confusion matrix, etc

import sys

if len(sys.argv) < 4:
	print 'usage: <labels.txt> <prediction.txt> <number_of_class>'
	sys.exit(1)

f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'r')
nc = int(sys.argv[3])

label = []
prediction = []
conf_matrix = [[0]*nc for x in xrange(nc)]

for line1 in f1.readlines():
	line2 = f2.readline()
	i = int(float(line1[:-1]))-1
	j = int(float(line2[:-1]))-1
	conf_matrix[i][j] += 1

print(' '.join(map(lambda x: str(x), range(1,nc+1))))
for i in xrange(nc):
	row = str(i+1)+' '
	for j in xrange(nc):
		row += str(conf_matrix[i][j]) +' '
	print row

# Calculate accuracy
acc = 0
total = 0
for i in xrange(nc):
	for j in xrange(nc):
		if i==j:
			acc += conf_matrix[i][j]
		total += conf_matrix[i][j]

print
print 'acc', str((float(acc)/total)*100)+'%', '('+str(acc)+'/'+str(total)+')'

# Precision and recall for each classes
precs = [0]*nc
recs = [0]*nc
for i in xrange(nc):
	precs[i] = conf_matrix[i][i]
	recs[i] = conf_matrix[i][i]
	prec_denom = 0
	rec_denom = 0
	for j in xrange(nc):
		prec_denom += conf_matrix[j][i]
		rec_denom += conf_matrix[i][j]
	if(prec_denom != 0):
		precs[i] = precs[i] / float(prec_denom)
	if(rec_denom != 0):
		recs[i] = recs[i] / float(rec_denom)

print
print 'precision'.rjust(23), 'recall'.rjust(15)
for i in xrange(nc):
	print 'class', (i+1), str(precs[i]).rjust(15), str(recs[i]).rjust(15)
