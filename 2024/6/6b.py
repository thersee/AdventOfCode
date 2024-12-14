from collections import defaultdict

with open('6/input.txt') as f:
    lines = f.read().splitlines()
    # lines = [int(x) for x in lines]

obstacles = defaultdict(int)



for row in range(0, len(lines)):
    for col in range(0, len(lines[row])):
        if lines[row][col] == '#':
            obstacles[(row,col)] = 1
        elif lines[row][col] == '^':
            startPos = (row, col)
            guardRow = row
            guardCol = col
            guardDir = (-1,0)

possibleObstacles = 0
for row in range(0, len(lines)):
    for col in range(0, len(lines[row])):
        if not (row, col) == startPos:
            guardRow = startPos[0]
            guardCol = startPos[1]
            guardDir = (-1,0)
            originalValue = obstacles[(row,col)]
            obstacles[(row,col)] = 1
            distinctPositions = set()
            #egentligen, har han varit på samma pos i samma riktning?
            while guardRow > -1 and guardRow < len(lines) and guardCol > -1 and guardCol < len(lines[0]):
                if (guardRow, guardCol, guardDir) in distinctPositions:
                    possibleObstacles += 1
                    break
                distinctPositions.add((guardRow, guardCol, guardDir))
                nextPos = (guardRow+guardDir[0], guardCol+guardDir[1])
                whatsThere = obstacles[nextPos]
                if whatsThere == 0:
                    guardRow = nextPos[0]
                    guardCol = nextPos[1]
                elif whatsThere == 1:
                    if guardDir == (-1,0):
                        guardDir = (0,1)
                    elif guardDir == (0,1):
                        guardDir = (1,0)
                    elif guardDir == (1,0):
                        guardDir = (0,-1)
                    elif guardDir == (0,-1):
                        guardDir = (-1,0)
            obstacles[(row,col)]  = originalValue

print(possibleObstacles)