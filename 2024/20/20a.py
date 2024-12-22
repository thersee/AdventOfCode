import sys
from queue import PriorityQueue
from collections import defaultdict
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

startPos = ()
goalPos = ()
walls = defaultdict(int)

for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] == '#':
            walls[(row,col)] = 1
        elif lines[row][col] == 'S':
            startPos = (row,col)
        elif lines[row][col] == 'E':
            goalPos = (row,col)

distance = defaultdict(int)
path = 0
pos = startPos
distance[pos] = path
while pos != goalPos:
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    for d in dirs:
        if walls[(pos[0]+d[0], pos[1]+d[1])] != 1 and (pos[0]+d[0], pos[1]+d[1]) not in distance.keys():
            pos = (pos[0]+d[0], pos[1]+d[1])
            path += 1
            distance[pos] = path
            continue

totalLenght = path

shortcuts = defaultdict(int)
numberOfShortCuts = 0
track = list(distance.keys())
for pos in track:
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    for d in dirs:
        if walls[(pos[0]+d[0], pos[1]+d[1])] == 1:
            for d2 in dirs:
                if (pos[0]+d[0]+d2[0], pos[1]+d[1]+d2[1]) != pos:
                    if pos[0]+d[0]+d2[0] >= 0 and pos[0]+d[0]+d2[0] < len(lines) and pos[1]+d[1]+d2[1] >= 0 and pos[1]+d[1]+d2[1] < len(lines[0]):
                        # if distance[(pos[0]+d[0]+d2[0], pos[1]+d[1]+d2[1])] != 1:
                        if distance[(pos[0]+d[0]+d2[0], pos[1]+d[1]+d2[1])] > 0:
                            lenght = distance[(pos[0]+d[0]+d2[0], pos[1]+d[1]+d2[1])] - distance[pos] -2 #(cheat time)
                            if lenght >= 100:
                                numberOfShortCuts += 1
                                shortcuts[lenght] += 1

print(numberOfShortCuts)
