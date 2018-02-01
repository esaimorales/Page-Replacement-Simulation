# Second Chance Algorithm
# Author: Esai Morales
# File: sc.py

import sys

CACHE_SIZE = int(sys.argv[1])
queue = []
second_chance = []
page_faults = 0
numbers_per_file = 0
cursor = 0

# increases cursor
# if value greater than length of array
# put cursor back to start of array
def increment_cursor():
    global cursor
    cursor += 1
    if cursor == CACHE_SIZE:
        cursor = 0

for line in sys.stdin:
    stripped = line.strip()

    # handle non-digit line entries
    try:
        value = int(stripped)
        numbers_per_file += 1
    except ValueError:
        continue

    if value in queue:
        # get index of value in queue
        # update its value to 1 in second_chance
        # list, don't increment cursor
        i = queue.index(value)
        second_chance[i] = 1

    elif value not in queue and len(queue) < CACHE_SIZE:
        # append value to end of queue
        # and initialize it's value in second_chace array to 0
        # according to its index in queue
        queue.append(value)
        second_chance.append(0)

        # update values
        page_faults+=1
        increment_cursor()
        print value

    elif value not in queue and len(queue) == CACHE_SIZE:
        # update values
        page_faults+=1
        print value

        # keeps cursor from exeeding index of list (round robin)
        while True:
            if second_chance[cursor] == 0:
                queue[cursor] = value
                second_chance[cursor] = 0
                increment_cursor()
                break
            else:
                second_chance[cursor] = 0
                increment_cursor()
                continue

# print to stderr 
print >> sys.stderr, 'page faults: ', page_faults
print >> sys.stderr, 'valid numbers in file: ', numbers_per_file
