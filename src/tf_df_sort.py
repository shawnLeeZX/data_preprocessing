#!/usr/bin/env python
# coding=utf-8


import sys
import numpy as np
# import math

if len(sys.argv) != 2:
    print '''Usage: python tf_idf_sort.py [FILE]
    Note:
    ========================
    FILE FORMAT should be: word<tab>tf:idf.
    Program will output three files, which sorts the word by tf, idf and tfidf
    separatedly.
    ======================='''
    exit(1)

# Read tf-idf information from file.
tfidf_filename  = sys.argv[1]
tfidf_file      = open(tfidf_filename, 'r')

# Get tfidf into dictionary.
word_tf_df_list = []

for line in tfidf_file:
    word, tfidf = line.split('\t')
    tf, idf     = tfidf.split(':')

    tf  = int(tf)
    idf = int(idf)

    word_tf_df_list += [(word, tf, idf)]

# Create numpy structured array.
dtype = [('word', 'S40'), ('tf', int), ('df', int)]

# Sort according to tf.
word_tf_df_array               = np.array(word_tf_df_list, dtype)
word_tf_df_array_sorted_by_tf  = np.sort(word_tf_df_array, order='tf')

# Save the result to file.
tf_result_file = open(sys.argv[1] + '.sorted_tf', 'w')
for item in word_tf_df_array_sorted_by_tf:
    tf_result_file.writelines(
            item['word'] + '\t' + 
            str(item['tf']) + ':' +
            str(item['df']) + '\n')

# Sort according to idf.
word_tf_df_array_sorted_by_df  = np.sort(word_tf_df_array, order='df')

# Save the result to file.
idf_result_file = open(sys.argv[1] + '.sorted_df', 'w')
for item in word_tf_df_array_sorted_by_df:
    idf_result_file.writelines(
            item['word'] + '\t' + 
            str(item['tf']) + ':' +
            str(item['df']) + '\n')

# NOTE: we are not dealing with tfidf as the way in search engine -- we will
# discard words that only occurr in a few document while search engine will try
# to keep it. So the following code for calculating tfidf will be commented. And
# they are not finished.

# # After sorting, the last item should collect the summation information.
# tf_sum  = word_tf_df_array_sorted_by_df[-1]['tf']
# df_sum = word_tf_df_array_sorted_by_df[-1]['df']

# # Use a new list to calculate (word, tfidf).
# word_tfidf_list = []
# for item in word_tf_df_list:
    # tfidf = math.log()
