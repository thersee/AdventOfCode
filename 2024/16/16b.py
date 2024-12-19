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
visited = defaultdict(int)
q.put((0, start[0], start[1], (0,1), [], False))

run = True
totalScoreLowest = 1000000000
steps = 0
visitedTiles = []
while run:
    steps += 1
    step = q.get()
    step[4].append((step[1], step[2]))
    if steps% 10000 == 0:
        print(step[0], step[1], step[2], step[3], q.qsize())
    if (step[1], step[2]) == end:
        totalScore = step[0]
        if totalScore < totalScoreLowest:
            totalScoreLowest = totalScore
        if totalScore == totalScoreLowest:
            print('hej hej', totalScore)
            visitedTiles.extend(step[4])
        else:
            print('totalScore', totalScore)
            run = False
    else:
        v = visited[(step[1]+step[3][0], step[2]+step[3][1])]
        # print(v)
        if lines[step[1]+step[3][0]][step[2]+step[3][1]] != '#' and (v == 0 or v+1 == step[0] or v < step[0]):
            q.put((step[0]+1, step[1]+step[3][0], step[2]+step[3][1], step[3], step[4].copy(), False))
        # print(step)
        # print(visited.keys())
        v = visited[(step[1], step[2])]
        # print(v)
        if not step[5] and (v == 0 or v+1000 == step[0] or v == step[0]):
            if step[3] == (0,1):
                q.put((step[0]+1000, step[1], step[2], (-1,0), step[4].copy(), True))
                q.put((step[0]+1000, step[1], step[2], (1,0), step[4].copy(), True))
            elif step[3] == (1,0):
                q.put((step[0]+1000, step[1], step[2], (0, -1), step[4].copy(), True))
                q.put((step[0]+1000, step[1], step[2], (0, 1), step[4].copy(), True))
            elif step[3] == (0,-1):
                q.put((step[0]+1000, step[1], step[2], (-1,0), step[4].copy(), True))
                q.put((step[0]+1000, step[1], step[2], (1,0), step[4].copy(), True))
            elif step[3] == (-1,0):
                q.put((step[0]+1000, step[1], step[2], (0, -1), step[4].copy(), True))
                q.put((step[0]+1000, step[1], step[2], (0, 1), step[4].copy(), True))
            visited[(step[1], step[2])] = step[0]

print(totalScore)
print(len(set(visitedTiles)))