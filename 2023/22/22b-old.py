from collections import defaultdict
from copy import deepcopy

with open('22/input.txt') as f:
    lines = f.read().splitlines()

class Brick:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1=int(x1)
        self.x2=int(x2)
        self.y1=int(y1)
        self.y2=int(y2)
        self.z1=int(z1)
        self.z2=int(z2)
        self.svartePetter = False
    
    def __lt__(self, other):
        myMinz = min(self.z1, self.z2)
        otherMinz = min(other.z1, other.z2)
        return myMinz < otherMinz

    def __eq__(self, other):
        return self.x1 == other.x1 and self.x2 == other.x2 and self.y1 == other.y1 and \
        self.y2 == other.y2 and self.z1 == other.z1 and self.z2 == other.z2

    def getLowestZ(self):
        return min(self.z1, self.z2)
    
    def getHighestZ(self):
        return max(self.z1, self.z2)

    def overlaps(self, other):
        if self.svartePetter or other.svartePetter:
            return False
        for sx in range(min(self.x1, self.x2), max(self.x1, self.x2)+1):
            for sy in range(min(self.y2,self.y1), max(self.y1,self.y2)+1):
                for ox in range(min(other.x2,other.x1), max(other.x1,other.x2)+1):
                    for oy in range(min(other.y1,other.y2), max(other.y2, other.y1)+1):
                        if (sx, sy) == (ox,oy):
                            return True
        return False

    def __str__(self):
        return "("+str(self.x1) + ","+str(self.x2)+")" +\
        "("+str(self.y1) + ","+str(self.y2)+")" + \
        "("+str(self.z1) + ","+str(self.z2)+")"

bricks = list()

bricksPerLevelTop = defaultdict(list)
bricksPerLevelBottom = defaultdict(list)

for line in lines:
    ends = line.split('~')
    f = ends[0].split(',')
    l = ends[1].split(',')
    bricks.append(Brick(f[0], l[0], f[1], l[1], f[2], l[2]))

def moveDown(brick, bricksPerLevelTop, bricksPerLevelBottom):
    while(True):
        z = brick.getLowestZ()
        if z == 1:
            bricksPerLevelTop[brick.getHighestZ()].append(brick)
            bricksPerLevelBottom[z].append(brick)
            return z
        else:
            canMoveDown = True
            for b in bricksPerLevelTop[z-1]:
                if brick.overlaps(b):
                    # print(str(brick) +' overlaps '+ str(b))
                    canMoveDown = False
                    break

            if canMoveDown:
                # print('%'*20)
                # for k in bricksPerLevelTop[brick.getHighestZ()]:
                    # print(k, brick)
                    # print(k == brick)
                # print(brick, ' should be removed')
                # print('%'*20)
                if brick in bricksPerLevelTop[brick.getHighestZ()]:
                    # print('remove' + str(brick))
                    bricksPerLevelTop[brick.getHighestZ()].remove(brick)
                if brick in bricksPerLevelBottom[brick.getLowestZ()]:
                    bricksPerLevelBottom[brick.getLowestZ()].remove(brick)
                brick.z1 = brick.z1-1
                brick.z2 = brick.z2-1
            else:
                bricksPerLevelTop[brick.getHighestZ()].append(brick)
                bricksPerLevelBottom[brick.getLowestZ()].append(brick)
                return z

def canMoveDown(brick, previousLevel):
    canMoveDown = True
    for b in previousLevel:
        if brick.overlaps(b):
            canMoveDown = False
            break
    return canMoveDown
    

bricks.sort()
for brick in bricks:
    # print(brick)
    moveDown(brick, bricksPerLevelTop, bricksPerLevelBottom)



maxNumberMoved = 0
for brick in bricks:
    # print("#"*50)
    # print(brick)
    brick.svartePetter = True
    numberMoved = 0
    bricks.sort()
    bricksCopy=deepcopy(bricks)
    bricksPerLevelTopCopy = deepcopy(bricksPerLevelTop)
    bricksPerLevelBottomCopy = deepcopy(bricksPerLevelBottom)
    for b in bricksCopy:
        if not b.svartePetter:
            if b.getLowestZ() > brick.getHighestZ():
                # print(b)
                oldZ = b.getLowestZ()
                newZ = moveDown(b, bricksPerLevelTopCopy, bricksPerLevelBottomCopy)
                # print(newZ)
                if newZ != oldZ:
                    # print(b, ' has moved')
                    numberMoved += 1


    # print(brick, numberMoved)
    brick.svartePetter = False
    maxNumberMoved += numberMoved

print(maxNumberMoved)

#1235 too low