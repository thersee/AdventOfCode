import sys
from queue import PriorityQueue

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

rays = PriorityQueue()
rays.put(startPos)
visited = set()
splitted = 0

while rays.qsize() > 0:
    curr = rays.get()
    curr = (curr[0]+1, curr[1])
    if curr[0] > len(lines):
        continue
    if curr in splitters:
        splitted += 1
        curr1 = (curr[0], curr[1]+1)
        curr2 = (curr[0], curr[1]-1)
        if curr1 not in visited:
            visited.add(curr1)
            rays.put(curr1)
        if curr2 not in visited:
            visited.add(curr2)
            rays.put(curr2)
    
    elif curr not in visited:
        visited.add(curr)
        rays.put(curr)

print(splitted)