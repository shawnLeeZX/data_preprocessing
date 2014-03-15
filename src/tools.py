#!/usr/bin/env python
# coding=utf-8

import sys

# By default Python 2 tries to convert unicode into bytes using the ascii codec.
# One approach to tackle this is to check sys.stdout's encoding, and if it's
# unknown (None) wrap it into a codecs.Writer that can handle all characters
# that may occur. UTF-8 is usually a good choice, but other codecs are possible.
def setupEncodingForStdio():
    if sys.stdout.encoding is None:
        import codecs
        Writer = codecs.getwriter("utf-8")
        sys.stdout = Writer(sys.stdout)
    if sys.stderr.encoding is None:
        sys.stderr = Writer(sys.stderr)
