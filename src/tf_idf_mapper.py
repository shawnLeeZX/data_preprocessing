#!/usr/bin/env python
# coding=utf-8

# Input format:     doc_id<tab>content
# Output format:    word_name<tab>occurrence_in_the_doc

import sys
import nltk

# Running & Debugging
# ===========================================
# NOTE: For debug. When testing, uncomment the following line.
import pdb
docs_filename   = sys.argv[1]
docs_file       = open(docs_filename, 'r')

# NOTE: For real running. When running on hadoop, uncomment this line.
# docs_file = sys.stdin
# ===========================================

# Heuristics of Shuai's knowledge.
# ===========================================
# Head and tail of sentences should be stripped.
should_stripped_chars = u'\n.?!~:;。？！：；～……'

# Symbol should not be regard as standalone symbol.
# Note that '-' is not in it, since hypen plays a great role in forming words,
# like one-life-time. The case that only one '-' regarded as a word is handled
# seperately.
punctuation = u'`\t ,./\\!?()+|@$#%^&\'\":’“”_*=;><~[]{},，'
number      = u'0123456789'

chars_should_not_in_word = punctuation + number

# Word with length beyond this should not be regarded as standalone symbol.
nonsense_word_len = 40
# ===========================================

# Initialization 
# ===========================================
# Dealing with coding.
# =================================================================
# By default Python 2 tries to convert unicode into bytes using the ascii codec.
# One approach to tackle this is to check sys.stdout's encoding, and if it's
# unknown (None) wrap it into a codecs.Writer that can handle all characters
# that may occur. UTF-8 is usually a good choice, but other codecs are possible.
if sys.stdout.encoding is None:
    import codecs
    Writer = codecs.getwriter("utf-8")
    sys.stdout = Writer(sys.stdout)
if sys.stderr.encoding is None:
    sys.stderr = Writer(sys.stderr)
# =================================================================

# Load necessary library.
# =================================================================
# Load nltk sentence seperator.
nltk.data.load('nltk:tokenizers/punkt/english.pickle')
# =================================================================

# Data structure.
# =================================================================
# We do word count statistics in the mapper function.
# To achieve this, the mapper will maintain a dictionary to quick check whether
# one word is in the dict of not. If it is, increment its count, otherwise add
# it in the dict with count one.
words_stat = {}
# ===========================================



# Now begins the main part.
# ===========================================
for doc in docs_file:
    # Get content of the doc.
    discarded, content = doc.split('\t', 1)

    # Break content into sentences.
    sentences = nltk.sent_tokenize(content)

    word_list_tmp = []
    # Break sentence into words.
    for sentence in sentences:
        # Since there exists multiple different encoding in the corpus, the
        # chars that are decoded other than utf-8 will be discarded.
        conversion_done = False
        while not conversion_done:
            try:
                sentence = unicode(sentence, 'utf-8')
                conversion_done = True
            except UnicodeDecodeError as decode_error:
                sentence = sentence[1:decode_error.args[2]] + sentence[decode_error.args[3] + 1:]

        sentence = sentence.strip(should_stripped_chars)
        word_list_tmp += nltk.word_tokenize(sentence)

    # Do words statistics while pruning punctuation and nonsense words.
    stemmer = nltk.stem.lancaster.LancasterStemmer()
    for word in word_list_tmp:
        # Remove words that are too long.
        if len(word) > nonsense_word_len:
            continue

        # Remove words contain special chars.
        contain_illegal_char = False
        for char in chars_should_not_in_word:
            if char in word:
                contain_illegal_char = True
                break;
        if contain_illegal_char:
            continue

        # Handle the case that there is only one hypen in the word.
        if word == '-':
            continue

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
