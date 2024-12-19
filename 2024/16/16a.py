from collections import defaultdict
from queue import PriorityQueue

with open('16/input.txt') as f:
    lines = f.read().splitlines()

q = PriorityQueue()

start = ()
end = ()

for row in range(len(lines)):
    line = lines[row]
    indStart = line.find('S')
    indEnd = line.find('E')
    if indStart > -1:
        start = (row, indStart)
    if indEnd > -1: 
        end = (row, indEnd)

#(score, row, col, dir)
visited = []
q.put((0, start[0], start[1], (0,1)))

run = True
totalScore = 0
steps = 0
while run:
    steps += 1
    step = q.get()
    if steps% 10000 == 0:
        print(step[0], step[1], step[2], q.qsize())
    if (step[1], step[2]) == end:
        run = False
        totalScore = step[0]
        break
    else:
        if lines[step[1]+step[3][0]][step[2]+step[3][1]] != '#' and (step[1]+step[3][0], step[2]+step[3][1]) not in visited:
            q.put((step[0]+1, step[1]+step[3][0], step[2]+step[3][1], step[3]))
        if (step[1], step[2]) not in visited:
            if step[3] == (0,1):
                q.put((step[0]+1000, step[1], step[2], (-1,0)))
                q.put((step[0]+1000, step[1], step[2], (1,0)))
            elif step[3] == (1,0):
                q.put((step[0]+1000, step[1], step[2], (0, -1)))
                q.put((step[0]+1000, step[1], step[2], (0, 1)))
            elif step[3] == (0,-1):
                q.put((step[0]+1000, step[1], step[2], (-1,0)))
                q.put((step[0]+1000, step[1], step[2], (1,0)))
            elif step[3] == (-1,0):
                q.put((step[0]+1000, step[1], step[2], (0, -1)))
                q.put((step[0]+1000, step[1], step[2], (0, 1)))
        visited.append((step[1], step[2]))

print(totalScore)