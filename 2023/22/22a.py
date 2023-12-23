from collections import defaultdict

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
    
    def __lt__(self, other):
        myMinz = min(self.z1, self.z2)
        otherMinz = min(other.z1, other.z2)
        return myMinz < otherMinz

    def getLowestZ(self):
        return min(self.z1, self.z2)
    
    def getHighestZ(self):
        return max(self.z1, self.z2)

    def overlaps(self, other):
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

def moveDown(brick):
    while(True):
        z = brick.getLowestZ()
        if z == 1:
            bricksPerLevelTop[brick.getHighestZ()].append(brick)
            bricksPerLevelBottom[z].append(brick)
            return
        else:
            canMoveDown = True
            for b in bricksPerLevelTop[z-1]:
                if brick.overlaps(b):
                    canMoveDown = False
                    break

            if canMoveDown:
                brick.z1 = brick.z1-1
                brick.z2 = brick.z2-1
            else:
                bricksPerLevelTop[brick.getHighestZ()].append(brick)
                bricksPerLevelBottom[brick.getLowestZ()].append(brick)
                return

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
    moveDown(brick)

# for i, ricks in bricksPerLevelBottom.items():
#     print(i)
#     for r in ricks:
#         print(r)
canDisintegrate = set()

for i in range(0, max(bricksPerLevelTop.keys())+1):
    for brick in bricksPerLevelTop[i]:
        # print(i, brick)
        newLayer = bricksPerLevelTop[i].copy()
        newLayer.remove(brick)
        canMove = False 
        for b in bricksPerLevelBottom[brick.getHighestZ()+1]:
            if canMoveDown(b, newLayer):
                # print(b, " can move down")
                canMove = True
                break
        if not canMove:
            canDisintegrate.add(brick)
        
# for b in canDisintegrate:
#     print(b)
        
print(len(canDisintegrate))

#501 too low
#544 too high
