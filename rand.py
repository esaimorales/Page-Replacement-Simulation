# Random Page Replacement Algorithm
# Author: Esai Morales
# File: rand.py

import sys
import random

# declare global variables
CACHE_SIZE = int(sys.argv[1])
# simulates the cache
queue = []
page_faults = 0
numbers_per_file = 0

# read every line in stdin
for line in sys.stdin:

    stripped = line.strip()

    # handle non-digit line entries
    try:
        # try casting line to integer
        value = int(stripped)
        numbers_per_file+= 1

    # skip over line
    except ValueError:
        # if can't cast entry, then skip over line
        continue

    # when value is not in queue
    if value not in queue:

        # and there is space for a value in the cache
        if len(queue) < CACHE_SIZE:
            # add value to end of cache
            queue.append(value)
            print value
            page_faults+=1

        # or if cache size reached its limit
        elif len(queue) == CACHE_SIZE:
            # get random valid index
            rand_index = random.randint(0, CACHE_SIZE - 1)
            # place value in cache at random valid index
            queue[rand_index] = value
            print value
            page_faults+=1

# output counter to stderr
print >> sys.stderr, 'page faults: ', page_faults
print >> sys.stderr, 'valid numbers in file: ', numbers_per_file
