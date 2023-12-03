with open('3/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines]

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def findNumber(row, col):
    number = lines[row][col]
    line = lines[row]
    index = col + 1
    while index < len(line) and line[index].isdigit():
        number += line[index]
        index += 1
    index = col - 1
    while index >= 0 and line[index].isdigit():
        number = line[index] + number
        index -= 1
    return int(number)
    


def findAdjacentNumbers(row, col):
    rows = [row -1, row, row +1]
    cols = [col-1, col, col+1]
    numberAdjacent = 0
    prodAdjacent = 1
    for r in rows:
        lastDetectedCol = -3   
        for c in cols:
            if r > -1 and r < len(lines) and c > -1 and c < len(lines[r]):
                if lines[r][c].isdigit():
                    if lastDetectedCol == c-1:
                        lastDetectedCol = c
                    else:
                        lastDetectedCol = c
                        print(row, col, lines[r][c])
                        numberAdjacent += 1
                        if numberAdjacent > 2:
                            return 0
                        prodAdjacent *= findNumber(r,c)
    if numberAdjacent == 2:
        # print(prodAdjacent)
        return prodAdjacent
    else:
        return 0

totalSum = 0

for index, line in enumerate(lines):
    stars = find(line, '*')
    # print(stars)
    for star in stars:
        totalSum += findAdjacentNumbers(index, star)
    
print(totalSum)