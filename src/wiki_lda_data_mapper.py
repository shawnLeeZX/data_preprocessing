#!/usr/bin/env python
# coding=utf-8


# Input format:     doc_id<tab>pure english words seperated by whitespace
# Output format:    word_name<tab>doc_id:count

import tools
import sys

if len(sys.argv) != 2:
    print '''Usage: python lda_data_mapper.py [DICT]
    Note:
    ========================
    Input format:     doc_id<tab>pure english words seperated by whitespace
    Output format:    word_name<tab>doc_id:count
    You should specify your dictionary!!!
    ======================='''
    exit(1)

# Running & Debugging
# ===========================================
# NOTE: For debug. When testing, uncomment the following line.
# docs_filename   = sys.argv[1]
# docs_file       = open(docs_filename, 'r')
# dict_filename   = sys.argv[2]

# NOTE: For real running. When running on hadoop, uncomment this line.
docs_file = sys.stdin
dict_filename   = sys.argv[1]
# ===========================================

# Initialization 
# ===========================================
# Dealing with coding.
# =================================================================
tools.setupEncodingForStdio()
# =================================================================
# Data structure.
# =================================================================
dictionary = tools.loadDict(dict_filename)
# =================================================================


# Now begins the main part.
# ===========================================
for line in docs_file:
    doc_id, doc = line.split('\t', 1)

    doc_id = int(doc_id)

    word_list   = doc.split(' ')
    token_list  = {}
    # Only count the occurrence of words(token) in dictionary.
    for word in word_list:
        if word not in dictionary:
            continue

        if word in token_list:
            token_list[word] += 1
        else:
            token_list[word] = 1

    for token in token_list:
        print token + '\t' + str(doc_id) + ':' + str(token_list[token])
