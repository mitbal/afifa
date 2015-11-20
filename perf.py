#!/usr/bin/env python

# Perform evaluation by comparing ground truth labels and prediction
# such as accuracy, confusion matrix, etc

import sys

epsilon = 1e-10

if len(sys.argv) < 5:
	print 'usage: <labels.txt> <prediction.txt> <class label 1> <class label 2>...'
	sys.exit(1)

f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'r')
# nc = int(sys.argv[3])
labels = sys.argv[3:]

prediction = []
conf_matrix = {}
for i in labels:
	conf_matrix[i] = {}
	for j in labels:
		conf_matrix[i][j] = 0
# conf_matrix = [[0]*nc for x in xrange(nc)]

for line1 in f1.readlines():
	line2 = f2.readline()
	# i = int(float(line1[:-1]))-1
	# j = int(float(line2[:-1]))-1
	i = line1[:-1]
	j = line2[:-1]
	conf_matrix[i][j] += 1

print
header = ''
for label in labels:
	header += label.rjust(12)
print header

for i in labels:
	row = i+' '
	for j in labels:
		row += str(conf_matrix[i][j]).rjust(10) +' '
	print row

# Calculate accuracy
acc = 0
total = 0
for i in labels:
	for j in labels:
		if i==j:
			acc += conf_matrix[i][j]
		total += conf_matrix[i][j]

print
print 'acc', str((float(acc)/total)*100)+'%', '('+str(acc)+'/'+str(total)+')'

# Precision and recall for each classes
precs = {}
recs = {}
for i in labels:
	precs[i] = conf_matrix[i][i]
	recs[i] = conf_matrix[i][i]
	prec_denom = 0
	rec_denom = 0
	for j in labels:
		prec_denom += conf_matrix[j][i]
		rec_denom += conf_matrix[i][j]
	if(prec_denom != 0):
		precs[i] = precs[i] / float(prec_denom)
	if(rec_denom != 0):
		recs[i] = recs[i] / float(rec_denom)

print
print 'precision'.rjust(23), 'recall'.rjust(15)
for i in labels:
	print 'class', i, str(precs[i]).rjust(15), str(recs[i]).rjust(15)

# F measure
fmeasure = {}
print
print 'f measure'
for i in labels:
	if (precs[i]+recs[i]) > epsilon:
		fmeasure[i] = (2*precs[i]*recs[i]) / (precs[i]+recs[i])
	else:
		fmeasure[i] = 0
	print 'class', i, ':', fmeasure[i]
