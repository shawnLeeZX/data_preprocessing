#!/usr/bin/env python
# coding=utf-8

import sys

dict_with_tf_df_filename = sys.argv[1]
dict_with_tf_df_file     = open(dict_with_tf_df_filename, 'r')

dict_filename = sys.argv[2]
dict_file     = open(dict_filename, 'w')

# Assign one unique doc_id to docs in wiki corpus starting from 1.
id = 0
for line in dict_with_tf_df_file:
    word, discarded = line.split('\t')
    dict_file.write(word + '\n')

# Finalization.
dict_with_tf_df_file.close()
dict_file.close()
