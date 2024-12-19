import sys
from queue import PriorityQueue
from collections import defaultdict

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()


input = lines[0].split(', ')
towels = defaultdict(list)

for t in input:
    towels[t[0]].append(t)

print(towels)
numberOfFits = 0
for line in lines[2:]:
    # print(line)
    found = False
    toTry = PriorityQueue()
    for t in towels[line[0]]:
        if line.startswith(t):
            remainingLine = line[len(t):]
            toTry.put((-1*len(remainingLine), remainingLine))
    while toTry.qsize() > 0 and not found:
        node = toTry.get()
        thisLine = node[1]
        print(node[1])
        # print(thisLine)
        for t in towels[thisLine[0]]:
            # print('hej')
            if thisLine == t:
                found = True
                numberOfFits += 1
                print(line)
                break
            elif thisLine.startswith(t):
                remainingLine = thisLine[len(t):]
                toTry.put((-1*len(remainingLine), remainingLine))
        


print(numberOfFits)
