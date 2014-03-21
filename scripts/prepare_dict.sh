#/bin/bash

if [ $# -ne 1 ]; then
  echo "usage: $0 <doc_file>"
  exit
fi

# This scripts will calculate term frequency(tf) and document frequency(df) for
# each word in the <doc_file> and sort them according to tf and df seperately
# and store the results in respectively file with name
# <doc_file>.tf_df.softed_by_tf and <doc_file>.tf_df.sorted_by_df in the same
# folder of <doc_file>.
#
# Use the two files generated to create your own dictionary for future usage.

# Note that the input format of <doc_file> should be:
# doc_id<tab>document content.
# Document content should be normal article with regular punctuations.

# Variable setup.
script_path=`readlink -f $0`
script_dir=`dirname $script_path`
project_root=`dirname $script_dir`

doc_file=$1

# Count tf and df of words in the doc and store it in with name
# <doc_file>.tf_df.
cat ${doc_file} \
    | python $project_root/src/tf_df_mapper.py \
    | sort -k 1,1 -t $'\t' \
    | python $project_root/src/tf_df_reducer.py > "${doc_file}.tf_df"
