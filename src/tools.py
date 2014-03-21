#!/usr/bin/env python
# coding=utf-8

import sys
import codecs

# By default Python 2 tries to convert unicode into bytes using the ascii codec.
# One approach to tackle this is to check sys.stdout's encoding, and if it's
# unknown (None) wrap it into a codecs.Writer that can handle all characters
# that may occur. UTF-8 is usually a good choice, but other codecs are possible.
def setupEncodingForStdio():
    if sys.stdout.encoding is None:
        Writer = codecs.getwriter("utf-8")
        sys.stdout = Writer(sys.stdout)
    if sys.stderr.encoding is None:
        sys.stderr = Writer(sys.stderr)

# Load dictionary from file as a list.
def loadDict(dict_filename):
    dict_list = []
    dict_file = open(dict_filename, 'r')

    for word in dict_file:
        word        = word.strip('\n')
        dict_list   += [word]

    return dict_list
