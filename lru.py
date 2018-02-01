# Least Recently Used algorithm
# Author: Esai Morales
# File: lru.py

import sys
from datetime import datetime

# set cache size
CACHE_SIZE = int(sys.argv[1])
queue = []                  # simulates cache
page_faults = 0
numbers_per_file = 0

# read from evey line
for line in sys.stdin:
    stripped = line.strip()

    # handle non-digit line entries
    try:
        value = int(stripped)
        numbers_per_file+= 1

    # skip over line
    except ValueError:
        continue

    # value exists in queue
    if value in queue:
        queue.remove(value) # remove item, place in the front
        queue.append(value)

    # value not in queue and space available
    elif value not in queue and len(queue) < CACHE_SIZE:
        queue.append(value) #add to front of queue
        print value
        page_faults+= 1

    # value not in queue and no space available
    elif (value not in queue) and (len(queue) == CACHE_SIZE):
        queue.pop(0)    # remove last item
        queue.append(value) # add new value to front 
        print value
        page_faults+= 1

# output results to stderr
# other opt - sys.stderr.write()
print >> sys.stderr, 'page faults: ', page_faults
print >> sys.stderr, 'valid numbers in file: ', numbers_per_file
