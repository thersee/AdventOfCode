import sys
from queue import Queue, PriorityQueue
from collections import defaultdict
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

def nextNumber(secret):
    #Multiply by 64
    n = secret * 64
    #Mix into secret
    secret = n ^ secret
    #prune
    secret = secret % 16777216 
    n = int(secret / 32)
    secret = n ^ secret
    secret = secret % 16777216 
    n = secret * 2048
    secret = n ^ secret
    secret = secret % 16777216 
    return secret

allDiffs = dict()
sequences = set()
for row, line in enumerate(lines):
    secret = int(line)
    rowDiffs = dict()
    diffs = []
    for i in range(2000):
        newSecret = nextNumber(secret)
        diff = str(newSecret%10-secret%10)
        diffs.append(diff)
        if i > 2:
            sequence =  ','.join(diffs[i-3:i+1])
            if sequence not in rowDiffs.keys():
                sequences.add(sequence)
                rowDiffs[sequence] = newSecret%10
        secret = newSecret
    allDiffs[row] = rowDiffs

print('calculated diffs', len(sequences))
maxGain = 0
for j, s in enumerate(sequences):
    if j %1000 == 0:
        print('sequence', j)
    thisGain = 0
    for i in range(len(lines)):
        if s in allDiffs[i]:
            thisGain += allDiffs[i][s]
    if thisGain > maxGain:
        maxGain = thisGain



print(maxGain)