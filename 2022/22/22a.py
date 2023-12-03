import re

with open('22/input.txt') as f:
    lines = f.read().splitlines()

posX=-1
posY=-1

theMap = dict()
for y in range(0, len(lines)):
    line = lines[y]
    if len(line) > 0 and line[0] == '1':
        directions = line
    for x in range(0, len(line)):
        if line[x] == ' ':
            continue
        elif line[x] == '.':
            if posX == -1:
                posX = x
                posY = y
            theMap[(x,y)] = '.'
        elif line[x] == '#':
            theMap[(x,y)] = '#'

lines.pop()
lines.pop()

dir = 0 #0=right,1=down,2=left,3=up
index = 0
nextDirChange = re.search('R|L', directions)
nextDirChange = nextDirChange.span()[0]

while index < len(directions):
    steps = int(directions[index:nextDirChange])
    index = nextDirChange
    inc = 0
    while inc < steps:
        if dir == 0:
            lastPosX = posX
            while lines[posY][(posX+1)%len(lines[posY])] == ' ':
                posX = (posX+1)%len(lines[posY])
            if lines[posY][(posX+1)%len(lines[posY])] == '.':
                posX = (posX+1)%len(lines[posY])
                lastPosX = posX
                inc += 1
            elif lines[posY][(posX+1)%len(lines[posY])] == '#':
                posX = lastPosX
                break

        elif dir == 1:
            lastPosY = posY
            while lines[(posY+1)%len(lines)][posX] == ' ':
                posY = (posY+1)%len(lines)
            if lines[(posY+1)%len(lines)][posX] == '.':
                posY = (posY+1)%len(lines)
                lastPosY = posY
                inc += 1
            elif lines[(posY+1)%len(lines)][posX] == '#':
                posY = lastPosY
                break

        elif dir == 2:
            lastPosX = posX
            while lines[posY][(posX-1)%len(lines[posY])] == ' ':
                posX = (posX-1)%len(lines[posY])
            if lines[posY][(posX-1)%len(lines[posY])] == '.':
                posX = (posX-1)%len(lines[posY])
                lastPosX = posX
                inc += 1
            elif lines[posY][(posX-1)%len(lines[posY])] == '#':
                posX = lastPosX
                break
        
            
        elif dir == 3:
            lastPosY = posY
            while lines[(posY-1)%len(lines)][posX] == ' ':
                posY = (posY-1)%len(lines)
            if lines[(posY-1)%len(lines)][posX] == '.':
                posY = (posY-1)%len(lines)
                lastPosY = posY
                inc += 1
            elif lines[(posY-1)%len(lines)][posX] == '#':
                posY = lastPosY
                break
    if index != len(directions):
        if directions[index] == 'R':
            dir = (dir + 1)%4
        else:
            dir = (dir -1)%4
        #print(posX, posY, dir)

        index += 1
        nextDirChange = re.search('R|L', directions[index:])
        if nextDirChange:
            nextDirChange = nextDirChange.span()[0]+index
        else:
            nextDirChange = len(directions)

print(posX+1, posY+1)
print(dir)
print((posY+1)*1000+(posX+1)*4+dir)