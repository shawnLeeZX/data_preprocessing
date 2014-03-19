#!/usr/bin/env python
# coding=utf-8

import sys

corpus_filename = sys.argv[1]
corpus_file     = open(corpus_filename, 'r')

corpus_with_doc_id_filename = corpus_filename + '.with_doc_id'
corpus_with_doc_id_file     = open(corpus_with_doc_id_filename, 'w')

# Assign one unique doc_id to docs in wiki corpus starting from 1.
id = 0
for doc in corpus_file:
    line = str(id) + '\t' + doc
    corpus_with_doc_id_file.write(line)
    id += 1

# Finalization.
corpus_file.close()
corpus_with_doc_id_file.close()
