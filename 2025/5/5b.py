import sys
from functools import cmp_to_key

with open(sys.argv[1]) as f:
    rawlines = f.read().splitlines()

def firstValue (a,b):
    return int(a.split('-')[0])-int(b.split('-')[0])

lines = list()
for line in rawlines:
    if line == '':
        break
    lines.append(line)


fresh = list()
lines = sorted(lines, key=cmp_to_key(firstValue))

empty = False
i = 0
for line in lines:
    if line == "":
        break
    ints = line.split('-')
    start = int(ints[0])
    end = int(ints[1])
    added = False
    #print(start,end)
    #print(fresh)
    newFresh = list()
    for pair in fresh:
        os = pair[0]
        oe = pair[1]
        ns = os
        ne = oe
        #print("all vals", os, oe, start, end)
        if start < os and end >= os:
            ns = start
            added = True
        if end > oe and start <= oe:
            ne = end
            added = True
        if start >= os and end <= oe:
            ns = os
            ne = oe
            added = True
        newFresh.append((ns,ne ))
    fresh = newFresh
    if not added:
        #print(start,end)
        #print("added")
        fresh.append((start,end))
    #print("#"*50)

totalFresh = 0
for pair in fresh:
    fresh = pair[1]-pair[0] +1
    totalFresh += fresh
print(totalFresh)