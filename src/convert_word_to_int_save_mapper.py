#!/usr/bin/env python

import sys
import tools
import codecs

if len(sys.argv) != 3:
    print '''Usage: python convert_url_to_int_save_map.py [FILE] [DICT_FILE]
    Note:
    ========================
    FILE FORMAT should be: word doc_id:word_count pairs.
    After converting, the file FORMAT will be word_id doc_id:word_count pairs.
    Save word mapping in file.
    ======================='''
    exit(1)


# Read document from file.
old_data_filename   = sys.argv[1]
old_data_file       = codecs.open(old_data_filename, encoding='utf-8', mode='r')

# Open new file to store coverted docs.
new_data_filename   = old_data_filename[:old_data_filename.rfind('.')] + '.lda_data'
new_data_file       = codecs.open(new_data_filename, encoding='utf-8', mode='w')

# Open new file to store word index map.
new_map_filename   = old_data_filename[:old_data_filename.rfind('.')] + '.map'
new_map_file        = codecs.open(new_map_filename, encoding='utf-8', mode='w')

dict_list = tools.loadDict(sys.argv[2])

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
