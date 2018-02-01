# Least Recently Used Algorithm
# Author: Esai Morales
# File: lfu.py

import sys

CACHE_SIZE = int(sys.argv[1])
queue = []
page_faults = 0
numbers_per_file = 0

for line in sys.stdin:
    stripped = line.strip()

    # handle non-digit line entries
    try:
        value = int(stripped)
        numbers_per_file += 1

    # skip over line
    except ValueError:
        continue

    values = [item[0] for item in queue]

    # if item in cache
    # pop it out and append it with incremented frequency
    if value in values:
        index = values.index(value)
        tup = queue.pop(index)
        tup[1]+= 1
        queue.append(tup)
        # sort by frequency
        queue = sorted(queue, key= lambda x: x[1])

    # if not in cache
    else:
        # if space available
        if len(queue) < CACHE_SIZE:
            # add to front
            queue.append([value, 1])
            # sort by frequency
            queue = sorted(queue, key= lambda x: x[1])
            print value
            page_faults+=1

        # if no space available
        elif len(queue) == CACHE_SIZE:
            # remove least frequent
            queue.pop(0)
            # add to front 
            queue.append([value, 1])
            # sort by frequency
            queue = sorted(queue, key= lambda x: x[1])
            print value
            # increase frequency value of item
            page_faults+=1

print >> sys.stderr, 'page faults: ', page_faults
print >> sys.stderr, 'valid numbers in file: ', numbers_per_file
