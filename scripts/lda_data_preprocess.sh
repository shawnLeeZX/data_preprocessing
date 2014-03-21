#/bin/bash

if [ $# -ne 2 ]; then
  echo "usage: $0 <doc_file> <dictionary>"
  exit
fi

# This script will create lda-style data file to be used in petuum.

# Note that the input format of <doc_file> should be:
# doc_id<tab>document content.
# Document content should be normal article with regular punctuations.

# Variable setup.
script_path=`readlink -f $0`
script_dir=`dirname $script_path`
project_root=`dirname $script_dir`

doc_file=$1
dict_file=$2

almost_lda_style_data="${doc_file}.almost_lda_data"

# Create data with almost lda-style.
cat ${doc_file} \
    | python ${project_root}/src/lda_data_mapper.py ${dict_file} \
    | sort -k 1,1 -t $'\t'  \
    | python ${project_root}/src/lda_data_reducer.py > ${almost_lda_style_data}

# Convert words in previously generated file into integer and log down map file
# for converted words.
python ${project_root}/src/convert_word_to_int_save_mapper.py \
    ${almost_lda_style_data} ${dict_file}
