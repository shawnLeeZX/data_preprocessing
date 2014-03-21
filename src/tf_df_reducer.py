#!/usr/bin/env python
# coding=utf-8

# Input format:     word<tab>count_in_doc
# Output format:    word_name<tab>tf:idf

import sys
import tools

# Running & Debugging
# ===========================================
# NOTE: For debug. When testing, uncomment the following line.
# import pdb
# word_counts_filename   = sys.argv[1]
# word_counts_file       = open(word_counts_filename, 'r')

# NOTE: For real running. When running on hadoop, uncomment this line.
word_counts_file = sys.stdin
# ===========================================

# Initialization 
# ===========================================
# Dealing with coding.
# Add this will result in error... so comment it. Unicode is strange...
# =================================================================
# tools.setupEncodingForStdio()
# =================================================================

# Data structure.
# =================================================================
current_word    = None
tf              = 0
# Different line means the word has been occurred in different files. To
# compute idf, just compute how many times the word has been occurred.
idf             = 0
# ===========================================


# Now begins the main part.
# ===========================================
for line in word_counts_file:
    word, count = line.split('\t', 1)
    count = int(count)

    if current_word != word:
        if current_word != None:
            print current_word + '\t' + str(tf) + ':' + str(idf)
        current_word = word
        tf  = count
        idf = 1
    else:
        tf  += count
        idf += 1

# Deal with the last line.
if current_word != None:
    print current_word + '\t' + str(tf) + ':' + str(idf)

