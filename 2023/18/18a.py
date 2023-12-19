from queue import Queue

with open('18/input.txt') as f:
    lines = f.read().splitlines()

edgeNodes = set()
row = 0
col = 0
minRow = 1000000000000
minCol = 1000000000000
maxRow = -1000000000000
maxCol = -1000000000000

edgeNodes.add((row, col))
for line in lines:
    vals = line.split(' ')
    dir = vals[0]
    num = int(vals[1])
    if dir == 'D':
        for i in range(0, num):
            row += 1
            if row> maxRow:
                maxRow = row
            edgeNodes.add((row, col))
    elif dir == 'U':
        for i in range(0, num):
            row -= 1
            if row < minRow:
                minRow = row
            edgeNodes.add((row, col))
    elif dir == 'L':
        for i in range(0, num):
            col -= 1
            if col < minCol:
                minCol = col
            edgeNodes.add((row, col))
    elif dir == 'R':
        for i in range(0, num):
            col += 1
            if col > maxCol:
                maxCol = col
            edgeNodes.add((row, col))

initPoint = (1,1) #How to find this??

inside = dict()

q = Queue()
q.put(initPoint)
counter = 0
while(not q.empty()):
    counter += 1
    if counter %100 == 0:
        print(counter, len(inside))

    space = q.get()
    # print(space)
    if space in edgeNodes:
        pass
    elif space in inside:
        pass
    else:
        inside[space] = True
        if not (space[0]+1, space[1]) in inside and not (space[0]+1, space[1]) in edgeNodes:
            q.put((space[0]+1, space[1]))
        if not (space[0]-1, space[1]) in inside and not (space[0]-1, space[1]) in edgeNodes:
            q.put((space[0]-1, space[1]))
        if not (space[0], space[1]+1) in inside and not (space[0], space[1]+1) in edgeNodes:
            q.put((space[0], space[1]+1))
        if not (space[0], space[1]-1) in inside and not (space[0], space[1]-1) in edgeNodes:
            q.put((space[0], space[1]-1))

# for row in range(minRow, maxRow+1):
#     line = ''
#     for col in range(minCol, maxCol+1):
#         if (row, col) in edgeNodes:
#             if (row,col) == (0,0):
#                 line += '0'
#             else:
#                 line += '#'
#         else:
#             line += '.'
#     print(line)

print(len(edgeNodes))