from collections import defaultdict

with open('15/input.txt') as f:
    lines = f.read().splitlines()

walls = defaultdict(int)
boxes = defaultdict(int)
robot = (0,0)

def canMove(row, col, dir, movedBoxes):
    if walls[(row+dir[0], col+dir[1])]:
        return False, []
    if boxes[(row+dir[0], col+dir[1])]:
        movedBoxes.append((row+dir[0], col+dir[1]))
        return canMove(row+dir[0], col+dir[1], dir, movedBoxes)
    return True, movedBoxes


newLine = False
for row in range(len(lines)):
    if not newLine:
        if len(lines[row]) == 0:
            newLine = True
        else:
            for col in range(len(lines[row])):
                if lines[row][col] == '#':
                    walls[(row, col)] = 1
                elif lines[row][col] == 'O':
                    boxes[(row, col)] = 1
                elif lines[row][col] == '@':
                    robot = (row, col)
    else:
        for col in range(len(lines[row])):
            # print(robot)
            # print(boxes)
            dir = lines[row][col]
            if dir == '^':
                can = canMove(robot[0], robot[1], (-1,0), [])
                # print('up', can)
                if can[0]:
                    robot = (robot[0]-1, robot[1])
                    can[1].reverse()
                    for box in can[1]:
                        boxes[box] = 0
                        boxes[(box[0]-1, box[1])] = 1
            elif dir == '>':
                can = canMove(robot[0], robot[1], (0,1), [])
                # print('right', can)
                if can[0]:
                    robot = (robot[0], robot[1]+1)
                    can[1].reverse()
                    for box in can[1]:
                        boxes[box] = 0
                        boxes[(box[0], box[1]+1)] = 1
            elif dir == 'v':
                can = canMove(robot[0], robot[1], (1,0), [])
                # print('down', can)
                if can[0]:
                    robot = (robot[0]+1, robot[1])
                    can[1].reverse()
                    for box in can[1]:
                        boxes[box] = 0
                        boxes[(box[0]+1, box[1])] =1
            elif dir == '<':
                can = canMove(robot[0], robot[1], (0,-1), [])
                # print('left', can)
                if can[0]:
                    robot = (robot[0], robot[1]-1)
                    can[1].reverse()
                    for box in can[1]:
                        boxes[box] = 0
                        boxes[(box[0], box[1]-1)] =1

gps = 0
for box in boxes.keys():
    if boxes[box]:
        gps += box[0]*100+box[1]
print(gps)