with open('10/input.txt') as f:
    lines = f.read().splitlines()

for row, line in enumerate(lines):
    col = line.find('S')
    if col > -1:
        startPos = (row, col)
        break

firstSteps = []
possibleS = []
if lines[row-1][col] in ['|', 'F', '7']:
    firstSteps.append([(row-1, col), startPos])
    possibleS.append(['|', 'J', 'L'])
if lines[row][col+1] in ['-', '7', 'J']:
    firstSteps.append([(row, col+1), startPos])
    possibleS.append(['_', 'L', 'F'])
if lines[row+1][col] in ['|', 'J', 'L']:
    firstSteps.append([(row+1, col), startPos])
    possibleS.append(['|', 'F', '7'])
if lines[row][col-1] in ['_', 'L', 'F']:
    firstSteps.append([(row, col-1), startPos])
    possibleS.append(['-', '7', 'J'])

realS = list(set(possibleS[0]) & set(possibleS[1]))[0]
line = lines[row]
line = line.replace('S', realS)
lines[row] = line


pos1 = firstSteps[0]
pos2 = firstSteps[1]

def nextStep(posArray):
    pos = posArray[0]
    row = pos[0]
    col = pos[1]
    lastPos = posArray[1]
    # print(row, col)
    if lines[pos[0]][pos[1]] == '|':
        nextPos = (row+1, col)
        if nextPos == lastPos:
            nextPos = (row-1, col)
    elif lines[pos[0]][pos[1]] == '-':
        nextPos = (row, col+1)
        if nextPos == lastPos:
            nextPos = (row, col-1)
    elif lines[pos[0]][pos[1]] == 'J':
        nextPos = (row-1, col)
        if nextPos == lastPos:
            nextPos = (row, col-1)
    elif lines[pos[0]][pos[1]] == 'L':
        nextPos = (row-1, col)
        if nextPos == lastPos:
            nextPos = (row, col+1)
    elif lines[pos[0]][pos[1]] == '7':
        nextPos = (row, col-1)
        if nextPos == lastPos:
            nextPos = (row+1, col)
    elif lines[pos[0]][pos[1]] == 'F':
        nextPos = (row+1, col)
        if nextPos == lastPos:
            nextPos = (row, col+1)
    return [nextPos, pos]

visited = dict()
visited[startPos] = True
visited[pos1[0]] = True
visited[pos2[0]] = True


while (pos1[0] != pos2[0]):
    # print(pos1, pos2)
    pos1 = nextStep(pos1)
    pos2 = nextStep(pos2)
    visited[pos1[0]] = True
    visited[pos2[0]] = True

# print(visited)

enclosed = 0

for x in range(0, len(lines)):
    inTheLoop = False
    lastBent = ''
    for y in range(0, len(lines[0])):
        char = lines[x][y]
        if (x,y) in visited:
            if char == '|':
                inTheLoop = not inTheLoop
            elif char == 'F':
                if lastBent == '':
                    lastBent = 'F'
            elif char == 'L':
                if lastBent == '':
                    lastBent = 'L'
            elif char == 'J':
                if lastBent == 'L':
                    lastBent = ''
                else:
                    lastBent = ''
                    inTheLoop = not inTheLoop
            elif char == '7':
                if lastBent == 'F':
                    lastBent = ''
                else:
                    lastBent = ''
                    inTheLoop = not inTheLoop
        else:
            if inTheLoop:
                # print(x,y)
                enclosed += 1

        


print(enclosed)