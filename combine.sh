# Combine multiple csv files into one
# The first argument is the output filename

output=$1
shift

first=$1
shift

cat $first > $output

for i in "$@"
do
    sed "1d" $i >> $output
done
