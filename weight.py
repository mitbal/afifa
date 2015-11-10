#!/usr/bin/env python
# Visualize weight importance from liblinear algorithm

import matplotlib.pyplot as plt
import seaborn as sns
import math
import sys

if len(sys.argv) < 3:
	print 'usage: <model_file> <header_file> <optional column number>'
	sys.exit(1)

model_file = sys.argv[1]
header_file = sys.argv[2]
if len(sys.argv) > 3:
    col = int(sys.argv[3])
else:
    col = 0
fmodel = open(model_file, 'r')
fheader = open(header_file, 'r')

for i in xrange(6):
	fmodel.readline()

c = col
weights = []
for line in fmodel:
	tokens = line.split()
	weights.append(float(tokens[c]))

plt.plot(weights)
plt.show()

header = fheader.readline()
header = header.split(',')

fmodel.close()
fheader.close()

nonzero = []
nonzero_label = []
epsilon = 10e-10
for i in xrange(len(weights)):
	if abs(weights[i]) > epsilon:
		nonzero.append(weights[i])
		nonzero_label.append(header[i])

index = [x-0.35 for x in range(len(nonzero))]
fig = plt.figure()
fig.autofmt_xdate()
barlist = plt.bar(index, nonzero, color='g')
plt.xlim([-0.5, index[-1]+1])

for idx, nz in enumerate(nonzero):
	if nz < 0:
		barlist[idx].set_color('r')

plt.xticks(range(len(nonzero)), nonzero_label, rotation=90)
plt.show()
