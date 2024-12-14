from collections import defaultdict

with open('6/input.txt') as f:
    lines = f.read().splitlines()
    # lines = [int(x) for x in lines]

distinctPositions = set()
obstacles = defaultdict(int)



for row in range(0, len(lines)):
    for col in range(0, len(lines[row])):
        if lines[row][col] == '#':
            obstacles[(row,col)] = 1
        elif lines[row][col] == '^':
            guardRow = row
            guardCol = col
            guardDir = (-1,0)


while guardRow > -1 and guardRow < len(lines) and guardCol > -1 and guardCol < len(lines[0]):
    distinctPositions.add((guardRow, guardCol))
    nextPos = (guardRow+guardDir[0], guardCol+guardDir[1])
    # print(guardRow, guardCol)
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

print(len(distinctPositions))

