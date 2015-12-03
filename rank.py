
# Evaluate by ranking
# Inspired by normalized discounted cumulative gain (NDCG), not really

import sys

if len(sys.argv) < 5:
    print 'usage: <labels.txt> <prediction.txt> <class label 1> <class label 2> ...'
    sys.exit(1)

flabel = open(sys.argv[1], 'r')
fpred = open(sys.argv[2], 'r')
cls = sys.argv[3:]

totalGain = 0
counter = 0
for lab in flabel:
    num_pred = int(fpred.readline().split(' ')[1])
    # print lab
    label = lab.rstrip()
    for i in xrange(num_pred):
        pred = fpred.readline().split(' ')[1].rstrip()

        if label == pred:
            totalGain += 1 / float(i+1)
        # print 'totalGain', totalGain
    counter += 1

score = totalGain / float(counter)

print
print 'rank score', score
