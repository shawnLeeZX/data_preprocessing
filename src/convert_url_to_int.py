#!/usr/bin/env python

import sys
import codecs

if len(sys.argv) != 2:
    print '''Usage: python convert_url_to_int.py [FILE]
    Note:
    ========================
    FILE FORMAT should be: URL<tab>CONTENT.
    After converting, the file FORMAT will be DOC_ID<tab>CONTENT.
    ======================='''
    exit(1)

# Set up necessary variables.
root_dir   = '/home/shawn/mine/code/msra/preprocessing/'
src_dir    = root_dir + 'src/'
data_dir   = root_dir + 'data/'

# Read document from file
old_docs_filename   = sys.argv[1]
old_docs_file       = open(old_docs_filename, 'r')

# Open new file to store coverted docs.
new_docs_filename   = old_docs_filename + '.with_doc_id'
new_docs_file       = codecs.open(new_docs_filename, 'w')


# Convert document url in the file into doc_id, which is int numbered from zero.
doc_id = 0
for line in old_docs_file:
    discarded, line = line.split('\t', 1)
    # Store new doc_id with content into new file.
    new_docs_file.write(str(doc_id) + '\t' + line)
    doc_id += 1

# Finalization
old_docs_file.close()
new_docs_file.close()
