# Split csv files into two files: training and testing
#!/bin/bash

ln=`wc -l $1 | cut -f 1 -d ' '`
mid=$(($ln/2))
head -n $mid $1 > split1.csv
head -n 1 $1 > split2.csv
tail -n +$(($mid+1)) $1 >> split2.csv
