import sys
from queue import PriorityQueue
from collections import defaultdict
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

towels = lines[0].split(', ')

@cache
def towelFits(towel, pattern):
    if towel == pattern:
        return 1
    if pattern.startswith(towel):
        fits = 0
        for t in towels:
            fit = towelFits(t, pattern[len(towel):])
            fits += fit
        return fits
    else:
        return 0
    
numberOfFits = 0
for line in lines[2:]:
    anyFits = False
    internalNbr = 0
    for t in towels:
        fit = towelFits(t, line)
        internalNbr += fit
        numberOfFits += fit
    # print(line, internalNbr)


print(numberOfFits)