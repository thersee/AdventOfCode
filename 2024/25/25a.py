import sys
from queue import Queue, PriorityQueue
from collections import defaultdict
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

keys = []
locks = []

for i in range(0, len(lines), 8): #&?
    # print(lines[i])
    if lines[i] == '#####':
        lock = []
        for c in range(len(lines[i])):
            for r in range(7):
                # print(lines[i+r])
                # print(r)
                if lines[i+r][c] == '.':
                    lock.append(r-1)
                    break
        locks.append(lock)
    if lines[i] == '.....':
        key = []
        for c in range(len(lines[i])):
            for r in range(7):
                # print(lines[i+r])
                # print(r)
                if lines[i+r][c] == '#':
                    key.append(7-r-1)
                    break
        keys.append(key)

# print(locks)
# print(keys)
pairsThatFit = 0
for lock in locks:
    for key in keys:
        # print(lock, key)
        fit = True
        for i in range(len(lines[0])):
            # print(lock[i], key[i])
            if lock[i]+key[i] > 5:
                fit = False
                break
        if fit:
            pairsThatFit += 1

print(pairsThatFit)