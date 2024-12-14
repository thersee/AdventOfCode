from collections import defaultdict

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
        ul = 0
        ur = 0
        dl = 0
        dr = 0
        if self.posRow > (rows-1)/2:
            if self.posCol > (cols-1)/2:
                dr += 1
            elif self.posCol < (cols-1)/2:
                dl += 1
        elif self.posRow < (rows-1)/2:
            if self.posCol > (cols-1)/2:
                ur += 1
            elif self.posCol < (cols-1)/2:
                ul += 1
        return (ul,ur,dl,dr)

def printMap(i):
    file1 = open("output.txt", "w")
    file1.write(str(i)+"*"*cols+'\n')
    for row in range(rows):
        line = ''
        for col in range(cols):
            if (row, col) in robotPositions.keys():
                line += '#'
            else:
                line += ' '
        file1.write(line+'\n')
    file1.write("*"*cols+'\n')
    file1.close()


robots = []
robotPositions = defaultdict(Robot)

for line in lines:
    p, v = line.split(' ')
    pos = p.split('=')[1].split(',')
    vel = v.split('=')[1].split(',')
    robots.append(Robot(int(pos[1]), int(pos[0]), int(vel[1]), int(vel[0])))

for i in range(10000):
    ul = 0
    ur = 0
    dl = 0
    dr = 0
    robotPositions = dict()
    for robot in robots:
        rul, rur, rdl, rdr = robot.takeStep()
        ul += rul
        ur += rur
        dl += rdl
        dr += rdr
        robotPositions[(robot.posRow, robot.posCol)] = robot
    
    printMap(i)
    # print(ul, ur, dl, dr)
 #13240
 #10150
 #13446