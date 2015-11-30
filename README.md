# Afifa: Processing Large Data Line by Line for Machine Learning Daily usage

Afifa is a collection of scripts written in python and bash to process large text files for various common routines in machine learning, such as normalization, summarizing confusion matrix, etc.

## Example
### Combining multiple csv files
Do you ever need to combine multiple csv files because you need to split it in the first place due to some system limitation? Now you can simply just run

`bash combine.sh output.csv input1.csv input2.csv ... inputn.csv`

### Split
Do you ever need to split a single csv file into two files, so it can be used for training and testing data? Now just execute

`bash split.sh input.csv output_dir`

The original files will be split into split1.csv and split2.csv in the specified output directory.

