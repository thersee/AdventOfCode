import sys
from queue import PriorityQueue
from collections import defaultdict

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

startPos = (-1,-1)
splitters = list()

for row in range(len(lines)):
    line = lines[row]
    for col in range(len(line)):
        if line[col] == 'S':
            startPos = (row,col)
        elif line[col] == '^':
            splitters.append((row,col))

rays = dict()
rays[startPos[1]] = 1

nextRays = defaultdict(int)
for row in range(1,len(lines)):
    line = lines[row]
    for col in range(len(line)):
        if col in rays.keys():
            if (row, col) in splitters:
                nextRays[col+1] += rays[col]
                nextRays[col-1] += rays[col]
            else:
                nextRays[col] += rays[col]
    rays = nextRays

    nextRays = defaultdict(int)

print(sum(rays.values()))
