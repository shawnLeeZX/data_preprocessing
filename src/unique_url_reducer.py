#!/usr/bin/env python

import sys

url_tmp             = None
occurrence_count    = 0

for line in sys.stdin:
    url, count = line.split('\t', 1)
    count = int(count)
    if url != url_tmp:
        if url_tmp:
            print '{0}\t{1}'.format(url_tmp, str(occurrence_count))
        url_tmp = url
        occurrence_count = count
    else:
        occurrence_count += count

# Print the last key-value pair.
print url_tmp + '\t' + str(occurrence_count)
