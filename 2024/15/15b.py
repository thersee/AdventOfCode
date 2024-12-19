from collections import defaultdict
from functools import cmp_to_key

with open('15/input.txt') as f:
    lines = f.read().splitlines()

walls = defaultdict(int)
boxes = defaultdict(int)
robot = (0,0)

def canMove(row, col, dir, initial):
    if dir == (0,1): #höger
        if initial:
            if walls[(row, col+1)]:
                return False, []
            if boxes[(row, col+1)]:
                res = canMove(row, col+1, dir, False)
                movedBoxes = [(row, col+1)]
                movedBoxes.extend(res[1])
                return res[0], movedBoxes
            return True, []
        else:
            if walls[(row, col+2)]:
                return False, []
            if boxes[(row, col+2)]:
                res = canMove(row, col+2, dir, False)
                movedBoxes = [(row, col+2)]
                movedBoxes.extend(res[1])
                return res[0], movedBoxes
            return True, []
    elif dir == (0,-1): #vänster
        if walls[(row, col-2)]:
            return False, []
        if boxes[(row, col-2)]:
            res = canMove(row, col-2, dir, False)
            movedBoxes = [(row, col-2)]
            movedBoxes.extend(res[1])
            return res[0], movedBoxes
        return True, []
    elif dir == (1,0): #up
        if walls[(row+1, col)] or walls[(row+1, col-1)]:
            return False, []
        if boxes[(row+1, col)]:
            res1 = canMove(row+1, col, dir, False)
            res2 = canMove(row+1, col+1, dir, False)
            if res1[0] and res2[0]:
                movedBoxes = [(row+1, col)]
                movedBoxes.extend(res1[1])
                movedBoxes.extend(res2[1])
                return True, movedBoxes
            else:
                return False, []
        if boxes[(row+1, col-1)]:
            res1 = canMove(row+1, col-1, dir, False)
            res2 = canMove(row+1, col, dir, False)
            if res1[0] and res2[0]:
                movedBoxes = [(row+1, col-1)]
                movedBoxes.extend(res1[1])
                movedBoxes.extend(res2[1])
                return True, movedBoxes
            else:
                return False, []
        return True, []
    
    elif dir == (-1,0): #up
        if walls[(row-1, col)] or walls[(row-1, col-1)]:
            return False, []
        if boxes[(row-1, col)]:
            res1 = canMove(row-1, col, dir, False)
            res2 = canMove(row-1, col+1, dir, False)
            if res1[0] and res2[0]:
                movedBoxes = [(row-1, col)]
                movedBoxes.extend(res1[1])
                movedBoxes.extend(res2[1])
                return True, movedBoxes
            else:
                return False, []
        if boxes[(row-1, col-1)]:
            res1 = canMove(row-1, col-1, dir, False)
            res2 = canMove(row-1, col, dir, False)
            if res1[0] and res2[0]:
                movedBoxes = [(row-1, col-1)]
                movedBoxes.extend(res1[1])
                movedBoxes.extend(res2[1])
                return True, movedBoxes
            else:
                return False, []
        return True, []

def sortSide(a,b):
    return a[1]-b[1]

newLine = False
for row in range(0, len(lines)):
    if not newLine:
        if len(lines[row]) == 0:
            newLine = True
        else:
            for col in range(len(lines[row])):
                if lines[row][col] == '#':
                    walls[(row, col*2)] = 1
                elif lines[row][col] == 'O':
                    boxes[(row, col*2)] = 1
                elif lines[row][col] == '@':
                    robot = (row, col*2)
    else:
        # print(boxes)
        # print('newLine')
        for col in range(len(lines[row])):
            # print(boxes)
            # print(robot)
            # print(boxes)
            dir = lines[row][col]
            # print(row, col, dir)
            if dir == '^':
                can = canMove(robot[0], robot[1], (-1,0), True)
                # print('up', can)
                if can[0]:
                    robot = (robot[0]-1, robot[1])
                    can[1].sort() # sortera bättre
                    for box in can[1]:
                        boxes[box] = 0
                        boxes[(box[0]-1, box[1])] = 1
            elif dir == '>':
                can = canMove(robot[0], robot[1], (0,1), True)
                # print('right', can)
                if can[0]:
                    robot = (robot[0], robot[1]+1)
                    sorted(can[1], key=cmp_to_key(sortSide), reverse=True) # sortera bättre
                    for box in can[1]:
                        boxes[box] = 0
                        boxes[(box[0], box[1]+1)] = 1
            elif dir == 'v':
                can = canMove(robot[0], robot[1], (1,0), True)
                # print('down', can)
                if can[0]:
                    robot = (robot[0]+1, robot[1])
                    can[1].sort(reverse=True) # sortera bättre
                    for box in can[1]:
                        boxes[box] = 0
                        boxes[(box[0]+1, box[1])] =1
            elif dir == '<':
                # print(boxes)
                can = canMove(robot[0], robot[1], (0,-1), True)
                # print('left', can)
                # print(boxes)
                if can[0]:

                    robot = (robot[0], robot[1]-1)
                    sorted(can[1], key=cmp_to_key(sortSide), reverse=True) # sortera bättre
                    for box in can[1]:
                        boxes[box] = 0
                        boxes[(box[0], box[1]-1)] =1

# print(boxes)
gps = 0
for box in boxes.keys():
    if boxes[box]:
        # print(box)
        gps += box[0]*100+box[1]
print(gps)

# 1567490 too high 