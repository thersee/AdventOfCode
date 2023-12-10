with open('10/input.txt') as f:
    lines = f.read().splitlines()

for row, line in enumerate(lines):
    col = line.find('S')
    if col > -1:
        startPos = (row, col)
        break
# print(startPos[0], startPos[1])
print(lines[row+1][col])
firstSteps = []
if lines[row-1][col] in ['|', 'F', '7']:
    firstSteps.append([(row-1, col), startPos])
if lines[row][col+1] in ['-', '7', 'J']:
    firstSteps.append([(row, col+1), startPos])
if lines[row+1][col] in ['|', 'J', 'L']:
    firstSteps.append([(row+1, col), startPos])
if lines[row][col-1] in ['_', 'L', 'F']:
    firstSteps.append([(row, col-1), startPos])

print(firstSteps)
pos1 = firstSteps[0]
pos2 = firstSteps[1]

def nextStep(posArray):
    pos = posArray[0]
    row = pos[0]
    col = pos[1]
    # print(posArray)
    lastPos = posArray[1]
    # print(lines[pos[0]][pos[1]])
    if lines[pos[0]][pos[1]] == '|':
        # print('nedåt')
        nextPos = (row+1, col)
        # print(nextPos)
        if nextPos == lastPos:
            # print('nej uppåt')
            nextPos = (row-1, col)
    elif lines[pos[0]][pos[1]] == '-':
        # print('öger')
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
        # print('7a')
        nextPos = (row, col-1)
        if nextPos == lastPos:
            nextPos = (row+1, col)
    elif lines[pos[0]][pos[1]] == 'F':
        nextPos = (row+1, col)
        if nextPos == lastPos:
            nextPos = (row, col+1)
    # print('nextpos', nextPos)
    return [nextPos, pos]

steps = 1
while (pos1[0] != pos2[0]):
    # print("#"*50)
    # print(pos1[0], pos2[0])
    pos1 = nextStep(pos1)
    # print(pos1)
    pos2 = nextStep(pos2)
    # print(pos2)
    steps += 1

print(steps)