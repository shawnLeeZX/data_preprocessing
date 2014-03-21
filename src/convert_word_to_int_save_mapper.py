#!/usr/bin/env python

import sys
import tools

if len(sys.argv) != 2:
    print '''Usage: python convert_url_to_int.py [FILE]
    Note:
    ========================
    FILE FORMAT should be: word doc_id:word_count pairs.
    After converting, the file FORMAT will be word_id doc_id:word_count pairs.
    ======================='''
    exit(1)


# Read document from file
old_data_filename   = sys.argv[1]
old_data_file       = open(old_data_filename, 'r')

# Open new file to store coverted docs.
new_data_filename   = old_data_filename + '.new'
new_data_file       = open(new_data_filename, 'w')

# Open new file to store word index map.
new_map_filename    = old_data_filename + '.map'
new_map_file        = open(new_map_filename, 'w')

dict_list = tools.loadDict('../data/wiki.dict')

# Convert word in the file into doc_id, which is int numbered from zero.
word_id = 0
for line in old_data_file:
    word, doc_id_word_count_pairs = line.split(' ', 1)

    # Store the index map of words.
    index = dict_list.index(word)
    new_map_file.write(str(index) + ' ' + str(word_id) + '\n')

    # Store new doc_id with content into new file.
    new_data_file.write(str(word_id) + ' ' + doc_id_word_count_pairs)
    word_id += 1

# Finalization
old_data_file.close()
new_data_file.close()
new_map_file.close()
