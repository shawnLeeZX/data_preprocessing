#!/usr/bin/env python
# coding=utf-8

import sys
import codecs
import nltk

# Heuristics of Shuai's knowledge for nlp preprocessing.
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

# Now begins functions.
# ===========================================
# By default Python 2 tries to convert unicode into bytes using the ascii codec.
# One approach to tackle this is to check sys.stdout's encoding, and if it's
# unknown (None) wrap it into a codecs.Writer that can handle all characters
# that may occur. UTF-8 is usually a good choice, but other codecs are possible.
# ====================================================================
def setupEncodingForStdio():
    Writer = codecs.getwriter('utf-8')
    if sys.stdout.encoding is None:
        sys.stdout = Writer(sys.stdout)
    if sys.stderr.encoding is None:
        sys.stderr = Writer(sys.stderr)

    Reader = codecs.getwriter('utf-8')
    if sys.stdin.encoding is None:
        sys.stdin = Reader(sys.stdin)

# Load dictionary from file as a list.
# ====================================================================
def loadDict(dict_filename):
    dict_list = []
    dict_file = open(dict_filename, 'r')

    for word in dict_file:
        word        = unicode(word.strip('\n'), 'utf-8')
        dict_list   += [word]

    return dict_list

# Get word list from regular article.
# ====================================================================
def getWordListFromArticle(article):
    # Break article into sentences.
    sentences = nltk.sent_tokenize(article)

    word_list = []
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
        word_list += nltk.word_tokenize(sentence)
    return word_list

# Check whether one word is a word that makes sense.
# ====================================================================
def checkWordValidation(word):
    # Remove words that are too long.
    if len(word) > nonsense_word_len:
        return False

    # Remove control chars.
    if len(word) == 1 and ord(word) <= 0x1f:
        return False

    # Remove '--'.
    if word == '--':
        return False

    # Remove words contain special chars.
    contain_illegal_char = False
    for char in chars_should_not_in_word:
        if char in word:
            contain_illegal_char = True
            break;
    if contain_illegal_char:
        return False

    # Handle the case that there is only one hypen in the word.
    if word == '-':
        return False

    return True
