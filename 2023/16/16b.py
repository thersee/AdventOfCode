with open('16/input.txt') as f:
    lines = f.read().splitlines()


def findValue(startPoint):
    beams = [startPoint]

    mirrors = dict()

    for row, line in enumerate(lines):
        for col in range(0, len(line)):
            if line[col] != '.':
                mirrors[(row, col)] = line[col]

    visited = set()
    cont = True
    while(cont):
        newBeams = list()
        for beam in beams:
            nextPosX = beam[0]
            nextPosY = beam[1]
            if beam[2] == 'r':
                nextPosY += 1
            elif beam[2] == 'l':
                nextPosY -= 1
            elif beam[2] == 'u':
                nextPosX -= 1
            elif beam[2] == 'd':
                nextPosX += 1
            
            # print(beam, nextPosX, nextPosY)
            if nextPosX < 0 or  nextPosX >= len(lines[0]) or nextPosY < 0 or nextPosY >= len(lines):
                pass
            elif not (nextPosX, nextPosY) in mirrors:
                newBeams.append((nextPosX, nextPosY, beam[2]))
            elif mirrors[(nextPosX, nextPosY)] == '|':
                if (beam[2] == 'r' or beam[2] == 'l'):
                    newBeams.append((nextPosX, nextPosY, 'u'))
                    newBeams.append((nextPosX, nextPosY, 'd'))
                else:
                    newBeams.append((nextPosX, nextPosY, beam[2]))

            
            elif mirrors[(nextPosX, nextPosY)] == '-':
                if (beam[2] == 'u' or beam[2] == 'd'):
                    newBeams.append((nextPosX, nextPosY, 'r'))
                    newBeams.append((nextPosX, nextPosY, 'l'))
                else:
                    newBeams.append((nextPosX, nextPosY, beam[2]))

            elif mirrors[(nextPosX, nextPosY)] == '\\' and (beam[2] == 'l'):
                newBeams.append((nextPosX, nextPosY, 'u'))
            elif mirrors[(nextPosX, nextPosY)] == '\\' and (beam[2] == 'u'):
                newBeams.append((nextPosX, nextPosY, 'l'))
            elif mirrors[(nextPosX, nextPosY)] == '\\' and (beam[2] == 'r'):
                newBeams.append((nextPosX, nextPosY, 'd'))
            elif mirrors[(nextPosX, nextPosY)] == '\\' and (beam[2] == 'd'):
                newBeams.append((nextPosX, nextPosY, 'r'))

            elif mirrors[(nextPosX, nextPosY)] == '/' and (beam[2] == 'l'):
                newBeams.append((nextPosX, nextPosY, 'd'))
            elif mirrors[(nextPosX, nextPosY)] == '/' and (beam[2] == 'u'):
                newBeams.append((nextPosX, nextPosY, 'r'))
            elif mirrors[(nextPosX, nextPosY)] == '/' and (beam[2] == 'r'):
                newBeams.append((nextPosX, nextPosY, 'u'))
            elif mirrors[(nextPosX, nextPosY)] == '/' and (beam[2] == 'd'):
                newBeams.append((nextPosX, nextPosY, 'l'))


        beams = newBeams
        # print(newBeams)
        oldLen = len(visited)
        visited.update(newBeams)
        newLen = len(visited)
        if oldLen == newLen:
            cont = False

    uniquePos = set()

    for i in range(0,10):
        row = ''
        for j in range(0,10):
            if (i,j) in uniquePos:
                row += '#'
            else:
                row += '.'
        # print(row)
                
    for point in visited:
        uniquePos.add((point[0], point[1]))
    return len(uniquePos)

maxVal = 0

startingPos = []
for i in range(0, len(lines)):
    startingPos.append((i, -1, 'r'))
    startingPos.append((i, len(lines), 'l'))

for j in range(0, len(lines[0])):
    startingPos.append((-1, j, 'd'))
    startingPos.append((len(lines[0]), j, 'u'))

for index, start in enumerate(startingPos):
    print(index, len(startingPos))
    e = findValue(start)
    if e > maxVal:
        maxVal = e

#Not proud, but runs in an hour or so...
print(maxVal)