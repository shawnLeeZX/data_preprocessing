#!/usr/bin/env python

import sys

for line in sys.stdin:
    line, discarded = line.split('\t', 1)
    print line + '\t1'
