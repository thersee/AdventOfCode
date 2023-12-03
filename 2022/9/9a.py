from collections import defaultdict

with open('9/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 

tailPoses = set()
tailPosX = 0
tailPosY = 0
headPosX = 0
headPosY = 0

tailPoses.add((tailPosX, tailPosY))
for line in lines:
    move = line.split(' ')
    
    for i in range(0, int(move[1])):
        d = move[0]
        if d == 'R':
            headPosX += 1   
            if abs(tailPosX-headPosX) == 2 and abs(tailPosY -headPosY) == 0:
                tailPosX += 1
            elif (abs(tailPosX-headPosX) == 2 and abs(tailPosY -headPosY) == 1) or (abs(tailPosX-headPosX) == 1 and abs(tailPosY -headPosY) == 2):
                tailPosX += 1
                tailPosY = headPosY

        elif d == 'L':
            headPosX -= 1
            if abs(tailPosX-headPosX) == 2 and abs(tailPosY -headPosY) == 0:
                tailPosX -= 1
            elif (abs(tailPosX-headPosX) == 2 and abs(tailPosY -headPosY) == 1) or (abs(tailPosX-headPosX) == 1 and abs(tailPosY -headPosY) == 2):
                tailPosX -= 1
                tailPosY = headPosY
        elif d == 'U':
            headPosY += 1
            if abs(tailPosX-headPosX) == 0 and abs(tailPosY -headPosY) == 2:
                tailPosY += 1
            elif (abs(tailPosX-headPosX) == 1 and abs(tailPosY -headPosY) == 2) or (abs(tailPosX-headPosX) == 1 and abs(tailPosY -headPosY) == 2):
                tailPosY += 1
                tailPosX = headPosX
        else:
            headPosY -= 1
            if abs(tailPosX-headPosX) == 0 and abs(tailPosY -headPosY) == 2:
                tailPosY -= 1
            elif (abs(tailPosX-headPosX) == 1 and abs(tailPosY -headPosY) == 2) or (abs(tailPosX-headPosX) == 1 and abs(tailPosY -headPosY) == 2):
                tailPosY -= 1
                tailPosX = headPosX

        tailPoses.add((tailPosX, tailPosY))

print(len(tailPoses))