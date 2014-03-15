#!/usr/bin/env python
# coding=utf-8

# Input format:     pure english words seperated by whilespace
# Output format:    word_name<tab>occurrence_in_the_doc

import tools
import nltk
import sys

# Running & Debugging
# ===========================================
# NOTE: For debug. When testing, uncomment the following line.
docs_filename   = sys.argv[1]
docs_file       = open(docs_filename, 'r')

# NOTE: For real running. When running on hadoop, uncomment this line.
# docs_file = sys.stdin
# ===========================================

# Initialization 
# ===========================================
# Dealing with coding.
# =================================================================
tools.setupEncodingForStdio()
# =================================================================

# Now begins the main part.
# ===========================================
for doc in docs_file:
    # We do word count statistics in the mapper function.
    # To achieve this, the mapper will maintain a dictionary to quick check whether
    # one word is in the dict of not. If it is, increment its count, otherwise add
    # it in the dict with count one.
    words_stat = {}

    word_list_tmp = doc.split()

    # Do words statistics while pruning punctuation and nonsense words.
    stemmer = nltk.stem.lancaster.LancasterStemmer()
    for word in word_list_tmp:
        # Do word stemming.
        word_stemmed = stemmer.stem(word)

        # If the word is already in the dict increase its count, otherwise add
        # it in.
        if word_stemmed in words_stat:
            words_stat[word_stemmed] += 1
        else:
            words_stat[word_stemmed] = 1

    # Print <word, count> pair.
    # At the same time, to get the term frequency sum, use "" as a special key
    # to count the term frequency sum in every doc.
    terms_sum = 0
    for word in words_stat:
        count = words_stat[word]
        word_count = word + '\t' + str(count)
        print word_count
        terms_sum += count

    # Print term frequency sum.
    print '' +'\t' + str(terms_sum)
