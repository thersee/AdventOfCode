with open('24/input.txt') as f:
    lines = f.read().splitlines()

leftWinds = list()
rightWinds = list()
upWinds = list()
downWinds = list()
walls = list()

for row in range(0, len(lines)):
    for col in range(0,len(lines[row])):
        if lines[row][col] == '>':
            rightWinds.append([row, col])
        elif lines[row][col] == '<':
            leftWinds.append([row, col])
        elif lines[row][col] == '^':
            upWinds.append([row, col])
        elif lines[row][col] == 'v':
            downWinds.append([row, col])
        elif lines[row][col] == '#':
            walls.append((row, col))


startPos = (0,1)
finish = (len(lines)-1, len(lines[0])-2)
nbrOfCols = len(lines[0])-2
nbrOfRows = len(lines)-2

def windInPos(row, col, minutes):
    for wRow, wCol in rightWinds:
        if wRow == row and (wCol+minutes-1)%nbrOfCols+1 == col:
            # print(1)
            return True
    for wRow, wCol in leftWinds:
        if wRow == row and (wCol-minutes-1)%nbrOfCols+1 == col:
            # print(2)
            return True
    for wRow, wCol in upWinds:
        if wCol == col and (wRow-minutes-1)%nbrOfRows+1 == row:
            # print(3)
            return True
    for wRow, wCol in downWinds:
        if wCol == col and (wRow+minutes-1)%nbrOfRows+1 == row:
            # print(4)
            return True
    return False

#print(upWinds)
#print(windInPos(1,2,3))
toVisit = [[(0,1), 0]]
visited = set()
visited.add((0,1,0))

while toVisit:
    nextPos, minutes = toVisit.pop(0)


    nextRow = nextPos[0]
    nextCol = nextPos[1]
    if nextPos == finish:
        print(minutes)
        break
    if (nextRow, nextCol, minutes+1) not in visited and not windInPos(nextRow, nextCol, minutes+1):
        toVisit.append(([(nextRow, nextCol), minutes+1]))
        visited.add((nextRow, nextCol, minutes+1))
    if (nextRow+1, nextCol) not in walls and nextRow+1 <= nbrOfRows+1 and (nextRow+1, nextCol, minutes+1) not in visited and not windInPos(nextRow+1, nextCol, minutes+1):
        toVisit.append(([(nextRow+1, nextCol), minutes+1]))
        visited.add((nextRow+1, nextCol, minutes+1))
    if (nextRow-1, nextCol) not in walls and nextRow-1 >= 0 and (nextRow-1, nextCol, minutes+1) not in visited and not windInPos(nextRow-1, nextCol, minutes+1):
        toVisit.append(([(nextRow-1, nextCol), minutes+1]))
        visited.add((nextRow-1, nextCol, minutes+1))
    if (nextRow, nextCol+1) not in walls and (nextRow, nextCol+1, minutes+1) not in visited and not windInPos(nextRow, nextCol+1, minutes+1):
        toVisit.append(([(nextRow, nextCol+1), minutes+1]))
        visited.add((nextRow, nextCol+1, minutes+1))
    if (nextRow, nextCol-1) not in walls and (nextRow, nextCol-1, minutes+1) not in visited  and not windInPos(nextRow, nextCol-1, minutes+1):
        toVisit.append(([(nextRow, nextCol-1), minutes+1]))
        visited.add((nextRow, nextCol-1, minutes+1))


toVisit = [[finish, minutes]]
visited = set()
visited.add((finish[0], finish[1],minutes))

while toVisit:
    nextPos, minutes = toVisit.pop(0)


    nextRow = nextPos[0]
    nextCol = nextPos[1]
    if nextPos == startPos:
        print(minutes)
        break
    if (nextRow, nextCol, minutes+1) not in visited and not windInPos(nextRow, nextCol, minutes+1):
        toVisit.append(([(nextRow, nextCol), minutes+1]))
        visited.add((nextRow, nextCol, minutes+1))
    if (nextRow+1, nextCol) not in walls and nextRow+1 <= nbrOfRows+1 and (nextRow+1, nextCol, minutes+1) not in visited and not windInPos(nextRow+1, nextCol, minutes+1):
        toVisit.append(([(nextRow+1, nextCol), minutes+1]))
        visited.add((nextRow+1, nextCol, minutes+1))
    if (nextRow-1, nextCol) not in walls and nextRow-1 >= 0 and (nextRow-1, nextCol, minutes+1) not in visited and not windInPos(nextRow-1, nextCol, minutes+1):
        toVisit.append(([(nextRow-1, nextCol), minutes+1]))
        visited.add((nextRow-1, nextCol, minutes+1))
    if (nextRow, nextCol+1) not in walls and (nextRow, nextCol+1, minutes+1) not in visited and not windInPos(nextRow, nextCol+1, minutes+1):
        toVisit.append(([(nextRow, nextCol+1), minutes+1]))
        visited.add((nextRow, nextCol+1, minutes+1))
    if (nextRow, nextCol-1) not in walls and (nextRow, nextCol-1, minutes+1) not in visited  and not windInPos(nextRow, nextCol-1, minutes+1):
        toVisit.append(([(nextRow, nextCol-1), minutes+1]))
        visited.add((nextRow, nextCol-1, minutes+1))

toVisit = [[startPos, minutes]]
visited = set()
visited.add((startPos[0], startPos[1],minutes))

while toVisit:
    nextPos, minutes = toVisit.pop(0)


    nextRow = nextPos[0]
    nextCol = nextPos[1]
    if nextPos == finish:
        print(minutes)
        break
    if (nextRow, nextCol, minutes+1) not in visited and not windInPos(nextRow, nextCol, minutes+1):
        toVisit.append(([(nextRow, nextCol), minutes+1]))
        visited.add((nextRow, nextCol, minutes+1))
    if (nextRow+1, nextCol) not in walls and nextRow+1 <= nbrOfRows+1 and (nextRow+1, nextCol, minutes+1) not in visited and not windInPos(nextRow+1, nextCol, minutes+1):
        toVisit.append(([(nextRow+1, nextCol), minutes+1]))
        visited.add((nextRow+1, nextCol, minutes+1))
    if (nextRow-1, nextCol) not in walls and nextRow-1 >= 0 and (nextRow-1, nextCol, minutes+1) not in visited and not windInPos(nextRow-1, nextCol, minutes+1):
        toVisit.append(([(nextRow-1, nextCol), minutes+1]))
        visited.add((nextRow-1, nextCol, minutes+1))
    if (nextRow, nextCol+1) not in walls and (nextRow, nextCol+1, minutes+1) not in visited and not windInPos(nextRow, nextCol+1, minutes+1):
        toVisit.append(([(nextRow, nextCol+1), minutes+1]))
        visited.add((nextRow, nextCol+1, minutes+1))
    if (nextRow, nextCol-1) not in walls and (nextRow, nextCol-1, minutes+1) not in visited  and not windInPos(nextRow, nextCol-1, minutes+1):
        toVisit.append(([(nextRow, nextCol-1), minutes+1]))
        visited.add((nextRow, nextCol-1, minutes+1))


