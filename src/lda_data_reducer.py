#!/usr/bin/env python
# coding=utf-8

# Input format:     word_name doc_id:count
# Output format:    word_name doc_id:count*

import sys
# import tools

# Running & Debugging
# ===========================================
# NOTE: For debug. When testing, uncomment the following line.
# count_filename   = sys.argv[1]
# count_file       = open(count_filename, 'r')

# NOTE: For real running. When running on hadoop, uncomment this line.
count_file = sys.stdin
# ===========================================


# Initialization 
# ===========================================
# Dealing with coding.
# =================================================================
# tools.setupEncodingForStdio()
# =================================================================

# Now begins the main part.
# ===========================================
current_word        = None
doc_id_count_pairs  = None

for line in count_file:
    line = line.strip('\n')
    word, doc_id_count_pair = line.split('\t')
    doc_id, count           = doc_id_count_pair.split(':')

    if current_word != word:
        if current_word != None:
            print current_word + ' ' + doc_id_count_pairs
        current_word = word
        doc_id_count_pairs = doc_id_count_pair
    else:
        doc_id_count_pairs += ' ' + doc_id_count_pair

if current_word != None:
    print current_word + ' ' + doc_id_count_pairs
