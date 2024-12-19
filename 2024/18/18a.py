import sys
from queue import PriorityQueue
from collections import defaultdict

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()


myPos = (0,0,0)
endPos = (70,70)

posQueue = PriorityQueue()
posQueue.put(myPos)
alreadyVisited = []
walls = defaultdict(int)

for i in range(1,len(lines)+1):
     line = lines[i-1].split(',')

     walls[(int(line[0]), int(line[1]))] = i

found = False
while not found:
    thisPos = posQueue.get()
    print(thisPos)
    if (thisPos[1], thisPos[2]) in alreadyVisited:
            continue
    elif (thisPos[1], thisPos[2]) == endPos:
        found = True
        numberOfSteps = thisPos[0]
    else:
        alreadyVisited.append((thisPos[1], thisPos[2]))
        if thisPos[1] < 0 or thisPos[1] > endPos[0] or thisPos[2] < 0 or thisPos[2] > endPos[1]:
            #  print('nejj')
             continue
        elif walls[(thisPos[1], thisPos[2])] > 0 and walls[(thisPos[1], thisPos[2])] < 1025:
            # print('vägg')
            continue
        else:
            dirs = [(1,0),(0,1),(-1,0),(0,-1)]
            # print('hej?')
            for d in dirs:
                posQueue.put((thisPos[0]+1, thisPos[1]+d[0], thisPos[2]+d[1]))

print(numberOfSteps)