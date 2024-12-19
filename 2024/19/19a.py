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
        return True
    if pattern.startswith(towel):
        anyFits = False
        for t in towels:
            fit = towelFits(t, pattern[len(towel):])
            anyFits = anyFits or fit
        return anyFits
    else:
        return False
    
numberOfFits = 0
for line in lines[2:]:
    print(line)
    anyFits = False
    for t in towels:
        fit = towelFits(t, line)
        anyFits = anyFits or fit 
    if anyFits:
        numberOfFits += 1

print(numberOfFits)