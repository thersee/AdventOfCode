from collections import defaultdict
with open('12/input.txt') as f:
    lines = f.read().splitlines()

alreadyCounted = defaultdict(int)

def findArea(letter, row, col, totalArea, totalPer):
    if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
        totalPer += 1
        return [totalArea, totalPer]
    
    thisLetter = lines[row][col]
    if thisLetter == letter:
        if (row, col) not in alreadyCounted:
            alreadyCounted[(row,col)] = 1
            totalArea += 1
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]

            for dir in dirs:
                newValues = findArea(letter, row+dir[0], col+dir[1], 0, 0)
                totalArea += newValues[0]
                totalPer += newValues[1]
            return [totalArea, totalPer]
        else:
            return [totalArea, totalPer]
    else:
        totalPer += 1
        return [totalArea, totalPer]

totalPrice = 0
for row in range(len(lines)):
    for col in range(len(lines[0])):
        letter = lines[row][col]
        if (row, col) not in alreadyCounted:
            vals = findArea(letter, row, col, 0, 0)
            totalPrice += vals[0]*vals[1]

print(totalPrice)