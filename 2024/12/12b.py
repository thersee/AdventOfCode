
from collections import defaultdict
with open('12/input.txt') as f:
    lines = f.read().splitlines()

alreadyCounted = defaultdict(int)
#Räkna hörn, antingen har A kompisar (uppe & höger) (uppe & vänster) 
# (eller nere) eller så har en granne kompisar i arean på samma positioner

def isLetter(letter, row, col):
    if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
        # hur gör man här då? 
        return False
    return lines[row][col] == letter

def isNotLetter(letter, row, col):
    if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
        return True
    return lines[row][col] != letter

def findArea(letter, row, col, totalArea, totalCorners):
    if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
        return [totalArea, totalCorners]
    
    thisLetter = lines[row][col]
    if thisLetter == letter:
        if (row, col) not in alreadyCounted:
            alreadyCounted[(row,col)] = 1
            totalArea += 1
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]
            if isNotLetter(letter, row+1, col) and isNotLetter(letter, row, col+1) and isNotLetter(letter, row+1, col+1):
                # print(1, letter, row, col)
                totalCorners += 1
            if isNotLetter(letter, row+1, col) and isNotLetter(letter, row, col-1) and isNotLetter(letter, row+1, col-1):
                # print(2, letter, row, col)
                totalCorners += 1
            if isNotLetter(letter, row-1, col) and isNotLetter(letter, row, col+1) and isNotLetter(letter, row-1, col+1):
                # print(3, letter, row, col)
                totalCorners += 1
            if isNotLetter(letter, row-1, col) and isNotLetter(letter, row, col-1) and isNotLetter(letter, row-1, col-1):
                # print(4, letter, row, col)
                totalCorners += 1

            for dir in dirs:
                newValues = findArea(letter, row+dir[0], col+dir[1], 0, 0)
                totalArea += newValues[0]
                totalCorners += newValues[1]
            return [totalArea, totalCorners]
        else:
            return [totalArea, totalCorners]
    else:
        corners = 0
        #Kommer dubbelräkna hörn som man kan komma till på flera sätt
        if isLetter(letter, row+1, col) and isLetter(letter, row, col+1):
            # print(5, thisLetter, row, col)
            corners += 1
        if isLetter(letter, row+1, col) and isLetter(letter, row, col-1):
            # print(6, thisLetter, row, col)
            corners += 1
        if isLetter(letter, row-1, col) and isLetter(letter, row, col+1):
            # print(7, thisLetter, row, col)
            corners += 1
        if isLetter(letter, row-1, col) and isLetter(letter, row, col-1):
            # print(8, thisLetter, row, col)
            corners += 1
        
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        neighbors = 0
        for d in dirs:
            if isLetter(letter, row+d[0], col+d[1]):
                neighbors += 1
        if corners:
            totalCorners += corners/(neighbors) #dela inte på corners utan grannar
        return [totalArea, totalCorners]

totalPrice = 0
# print(findArea('A', 0, 0, 0, 0))
for row in range(len(lines)):
    for col in range(len(lines[0])):
        letter = lines[row][col]
        if (row, col) not in alreadyCounted:
            vals = findArea(letter, row, col, 0, 0)
            # print(letter, vals)
            totalPrice += vals[0]*round(vals[1])

print(totalPrice)