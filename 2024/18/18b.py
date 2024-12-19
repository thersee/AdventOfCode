import sys
from queue import PriorityQueue
from collections import defaultdict

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()




walls = defaultdict(int)
for i in range(1,len(lines)+1):
     line = lines[i-1].split(',')

     walls[(int(line[0]), int(line[1]))] = i

noPathFound = False

#man borde nog kunna göra en smart halveringssökgrej
for i in range(3027, len(lines)):
    if noPathFound:
        print('no path found', i-1)
        print(lines[i-3])
        break
    myPos = (0,0,0)
    endPos = (70,70)

    posQueue = PriorityQueue()
    posQueue.put(myPos)
    alreadyVisited = []
    found = False
    noPathFound = False
    while not found and not noPathFound:
        if posQueue.qsize() == 0:
            noPathFound = True
            continue
        thisPos = posQueue.get()
        # print(thisPos)
        if (thisPos[1], thisPos[2]) in alreadyVisited:
                continue
        elif (thisPos[1], thisPos[2]) == endPos:
            found = True
            numberOfSteps = thisPos[0]
        else:
            alreadyVisited.append((thisPos[1], thisPos[2]))
            if thisPos[1] < 0 or thisPos[1] > endPos[0] or thisPos[2] < 0 or thisPos[2] > endPos[1]:
                continue
            elif walls[(thisPos[1], thisPos[2])] > 0 and walls[(thisPos[1], thisPos[2])] < i:
                continue
            else:
                dirs = [(1,0),(0,1),(-1,0),(0,-1)]
                for d in dirs:
                    posQueue.put((thisPos[0]+1, thisPos[1]+d[0], thisPos[2]+d[1]))

    # print(numberOfSteps)
print('end')
