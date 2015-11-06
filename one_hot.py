# Perform one hot encoding
import sys
from subprocess import call

if len(sys.argv) < 4:
    print 'The usage is one_hot.py <input_file> <output_file> <header_file>'
    sys.exit(0)

call(['onehot_header.py', sys.argv[1], sys.argv[3]])

call(['onehot_apply.py', sys.argv[1], sys.argv[2], sys.argv[3], 'csv'])
