#!/usr/bin/env python
# coding=utf-8

import sys
import numpy as np

# Read tf-idf information from file.
tfidf_filename  = sys.argv[1]
tfidf_file      = open(tfidf_filename, 'r')

# Get tfidf into dictionary.
word_tf_idf_list = []

for line in tfidf_file:
    word, tfidf = line.split('\t')
    tf, idf     = tfidf.split(':')

    tf  = int(tf)
    idf = int(idf)

    word_tf_idf_list += [(word, tf, idf)]

# Create numpy structured array.
dtype = [('word', 'S40'), ('tf', int), ('idf', int)]

# Sort according to tf.
word_tf_idf_array               = np.array(word_tf_idf_list, dtype)
word_tf_idf_array_sorted_by_tf  = np.sort(word_tf_idf_array, order='tf')

# Save the result to file.
tf_result_file = open(sys.argv[1] + '.sorted_tf', 'w')
tf_result_file.writelines(
        'word' + '\t' + 
        'tf' + '\t' + 
        'idf' + '\n')
for item in word_tf_idf_array_sorted_by_tf:
    tf_result_file.writelines(
            item['word'] + '\t' + 
            str(item['tf']) + '\t' +
            str(item['idf']) + '\n')

# Sort according to idf.
word_tf_idf_array_sorted_by_idf  = np.sort(word_tf_idf_array, order='idf')

# Save the result to file.
idf_result_file = open(sys.argv[1] + '.sorted_idf', 'w')
idf_result_file.writelines(
        'word' + '\t' + 
        'tf' + '\t' + 
        'idf' + '\n')
for item in word_tf_idf_array_sorted_by_idf:
    idf_result_file.writelines(
            item['word'] + '\t' + 
            str(item['tf']) + '\t' +
            str(item['idf']) + '\n')
