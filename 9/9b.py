from collections import defaultdict

with open('9/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 

tailPoses = set()
currentPos = list()

def makeMove(i,j):
    headPosX = currentPos[i][0]
    headPosY = currentPos[i][1]
    tailPosX = currentPos[j][0]
    tailPosY = currentPos[j][1]

    if abs(tailPosX-headPosX) == 2 and abs(tailPosY -headPosY) == 0:
        if headPosX > tailPosX:
            tailPosX += 1
        else:
            tailPosX -= 1
    elif abs(tailPosX-headPosX) == 0 and abs(tailPosY -headPosY) == 2:
        if headPosY > tailPosY:
            tailPosY += 1
        else:
            tailPosY -= 1
    elif (abs(tailPosX-headPosX) == 2 and abs(tailPosY -headPosY) == 1):
        tailPosY = headPosY
        if headPosX > tailPosX:
            tailPosX += 1
        else:
            tailPosX -= 1
    elif (abs(tailPosX-headPosX) == 1 and abs(tailPosY -headPosY) == 2):
        tailPosX = headPosX
        if headPosY > tailPosY:
            tailPosY += 1
        else:
            tailPosY -= 1
    elif (abs(tailPosX-headPosX) == 2 and abs(tailPosY -headPosY) == 2):
        if headPosX > tailPosX:
            tailPosX += 1
        else:
            tailPosX -= 1
        if headPosY > tailPosY:
            tailPosY += 1
        else:
            tailPosY -= 1

    currentPos[j] = [tailPosX, tailPosY]

for i in range(0,10):
    currentPos.append([0,0])


tailPoses.add((0, 0))

for line in lines:
    move = line.split(' ')
    
    for i in range(0, int(move[1])):
        d = move[0]
        headPosX = currentPos[0][0]
        headPosY = currentPos[0][1]
        if d == 'R':
            headPosX += 1
        elif d == 'L':
            headPosX -= 1
        elif d == 'U':
            headPosY += 1
        else:
            headPosY -= 1

        currentPos[0] = [headPosX, headPosY]
        for j in range(0,len(currentPos)-1):
            makeMove(j,j+1)
            if j+1 == len(currentPos)-1:
                tailPoses.add((currentPos[j+1][0], currentPos[j+1][1]))



print(len(tailPoses))