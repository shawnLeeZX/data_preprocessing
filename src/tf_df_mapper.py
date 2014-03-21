#!/usr/bin/env python
# coding=utf-8

# Script Description
# ===========================================
# The script acts like normal map-reduce streamming workflow -- it takes input
# from stdin and print the result into stdout.
# Input format:     doc_id<tab>article
# Output format:    word_name<tab>word_count
#
# Article is normal article with punctuations.
# ===========================================


import nltk
import tools
import sys

# Running & Debugging
# ===========================================
# NOTE: For debug. When testing, uncomment the following line.
# import codecs
# docs_filename   = sys.argv[1]
# docs_file       = open(docs_filename, 'r')

# NOTE: For real running. When running on hadoop, uncomment this line.
docs_file = sys.stdin
# ===========================================


# Initialization 
# ===========================================
# Dealing with coding.
# =================================================================
tools.setupEncodingForStdio()
# =================================================================

# Load necessary library.
# =================================================================
# Load nltk sentence seperator.
nltk.data.load('nltk:tokenizers/punkt/english.pickle')
# =================================================================


# Now begins the main part.
# ===========================================
for doc in docs_file:
    # We do word count statistics in the mapper function.
    # To achieve this, the mapper will maintain a dictionary to quick check whether
    # one word is in the dict of not. If it is, increment its count, otherwise add
    # it in the dict with count one.
    words_stat = {}

    # Get article of the doc.
    discarded, article = doc.split('\t', 1)

    word_list = tools.getWordListFromArticle(article)

    # Do words statistics while pruning punctuation and nonsense words.
    for word in word_list:
        is_valid = tools.checkWordValidation(word)
        if is_valid:
            # If the word is already in the dict increase its count, otherwise
            # add it in.
            if word in words_stat:
                words_stat[word] += 1
            else:
                words_stat[word] = 1


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
