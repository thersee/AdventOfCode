with open('23/input.txt') as f:
    lines = f.read().splitlines()

elves = dict()
id = 1

for row in range(0, len(lines)):
    for col in range(0, len(lines[row])):
        if lines[row][col] == '#':
            elves[(row, col)] = id
            id += 1

def flatten(l):
    return [item for sublist in l for item in sublist]

def shouldMove(row, col, directions):
    shouldMove = False
    for dir in flatten(directions):

        if (row+dir[0], col+dir[1]) in elves:
            shouldMove = True
            break
    
    if shouldMove:
        for dir in directions:
            if (row+dir[0][0], col+dir[0][1]) not in elves and \
                (row+dir[1][0], col+dir[1][1]) not in elves and \
                (row+dir[2][0], col+dir[2][1]) not in elves:
                return (row+dir[1][0], col+dir[1][1]) 
    return (row,col)



round = 0
north = [(-1,-1), (-1,0),(-1,1)]
south = [(1,-1), (1,0), (1,1)]
west = [(-1, -1), (0,-1), (1,-1)]
east = [(-1,1), (0,1), (1,1)]

directions = [north, south, west, east]

while round < 10:
    toMove = dict()
    toRemove = list()
    for elf, id in elves.items():
        newPos = shouldMove(elf[0], elf[1], directions)
        if newPos != elf and newPos not in toMove:
            toMove[newPos] = [elf, id]
            toRemove.append(elf)
        elif newPos in toMove:
            oldElf = toMove.pop(newPos)
            toRemove.remove(oldElf[0])
    
    for elf, id in toMove.items():
        elves[elf] = id[-1]

    for elf in toRemove:
        elves.pop(elf)
    
    d = directions.pop(0)
    directions.append(d)
    round += 1
    # print(elves)
    # for i in range(-20,20):
    #     row = ''
    #     for j in range(-20,20):
    #         if (i,j) in elves:
    #             row += '#'
    #         else:
    #             row += '.'
    #     print(row)
    # print('#'*30)

first = list(elves)[0]
maxRow = minRow = first[0]
maxCol = minCol = first[1]
for (row, col) in elves:
    if row < minRow:
        minRow = row
    if row > maxRow:
        maxRow = row
    if col < minCol:
        minCol = col
    if col > maxCol:
        maxCol = col

totalArea = (1+maxRow -minRow)*(1+maxCol-minCol)
empty = totalArea - len(elves)
print(empty)


        


        