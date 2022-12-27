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


dirs = {0: (1,0), 1:(0, 1), 2: (-1,0), 3: (0,-1)}
dir = 0 #0=right,1=down,2=left,3=up
index = 0
nextDirChange = re.search('R|L', directions)
nextDirChange = nextDirChange.span()[0]

while index < len(directions):
    steps = int(directions[index:nextDirChange])
    index = nextDirChange
    inc = 0
    while inc < steps:
        nextX = posX+dirs[dir][0]
        nextY = posY+dirs[dir][1]

        nextdir = dir
        if (nextX, nextY) not in theMap:
            print(nextX, nextY)
            if nextY < 0 and nextX >= 50 and nextX < 100:
                nextY = nextX + 100
                nextX = 0
                nextdir = 0
            elif nextY < 0 and nextX >= 100 and nextX < 150:
                nextX = nextX - 100
                nextY = 199
                nextdir = 3
            elif nextY == 50 and nextX >= 100 and nextX < 150:
                nextY = nextX -50
                nextX = 99
                nextdir = 2
            elif nextY == 99  and nextX >= 0 and nextX < 50:
                nextY = nextX + 50
                nextX = 50
                nextdir = 0
            elif nextY == 200  and nextX >= 0 and nextX < 50:
                nextX = nextX + 100
                nextY = 0
                nextdir = 1
            elif nextY == 150 and nextX >= 50 and nextX < 100:
                nextY =nextX +100
                nextX = 49
                nextdir = 2

            elif nextX < 0 and nextY >= 150:
                nextX = nextY - 100
                nextY = 0
                nextdir =1
            elif nextX < 0 and nextY >= 100 and nextY < 150:
                nextY = 149 - nextY
                nextX = 50
                nextdir = 0
                
            elif nextX == 49 and nextY >= 50 and nextY < 100:
                nextX = nextY - 50
                nextY = 100
                nextdir = 1

            elif nextX == 49 and nextY >= 0 and nextY < 50:
                nextY = 149 - nextY
                nextX = 0
                nextdir = 0
            elif nextX == 50 and  nextY >= 150 and nextY < 200:
                nextX = nextY - 100
                nextY = 149
                nextdir = 3
            elif nextX == 100 and nextY >= 100 and nextY < 150:
                nextY = 149 - nextY
                nextX = 149
                nextdir = 2
            elif nextX == 100 and nextY >= 50 and nextY < 100:
                nextX = nextY + 50
                nextY = 49
                nextdir = 3
            elif nextX == 150:
                nextY = 149-nextY
                nextX = 99
                nextdir = 2


        if theMap[(nextX, nextY)] == '.':
            posX = nextX
            posY = nextY
            dir = nextdir
            inc += 1
        else:
            break
            


    if index != len(directions):
        if directions[index] == 'R':
            dir = (dir + 1)%4
        else:
            dir = (dir -1)%4
        
        index += 1
        nextDirChange = re.search('R|L', directions[index:])
        if nextDirChange:
            nextDirChange = nextDirChange.span()[0]+index
        else:
            nextDirChange = len(directions)

print(posX+1, posY+1)
print(dir)
print((posY+1)*1000+(posX+1)*4+dir)