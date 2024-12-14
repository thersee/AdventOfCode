with open('14/input.txt') as f:
    lines = f.read().splitlines()

rows = 103
cols = 101
class Robot:
    def __init__(self, posRow, posCol, velRow, velCol):
        self.posRow = posRow
        self.posCol = posCol
        self.velRow = velRow
        self.velCol = velCol
    
    def takeStep(self):
        self.posRow += self.velRow
        self.posCol += self.velCol
        self.posRow = self.posRow % rows
        self.posCol = self.posCol % cols

robots = []

for line in lines:
    p, v = line.split(' ')
    pos = p.split('=')[1].split(',')
    vel = v.split('=')[1].split(',')
    robots.append(Robot(int(pos[1]), int(pos[0]), int(vel[1]), int(vel[0])))

for i in range(100):
    for robot in robots:
        robot.takeStep()

ul = 0
ur = 0
dl = 0
dr = 0
for robot in robots:
    if robot.posRow > (rows-1)/2:
        if robot.posCol > (cols-1)/2:
            dr += 1
        elif robot.posCol < (cols-1)/2:
            dl += 1
    elif robot.posRow < (rows-1)/2:
        if robot.posCol > (cols-1)/2:
            ur += 1
        elif robot.posCol < (cols-1)/2:
            ul += 1

print(ul* ur* dl* dr)
