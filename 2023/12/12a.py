import re

with open('12/input.txt') as f:
    lines = f.read().splitlines()


def findBroken(str, 
                nbrOfBrokenList, 
                currentBrokenInRow, oldStr):
    # print(oldStr, str)
    if (len(str) == 0):
        if len(nbrOfBrokenList) == 0 or (len(nbrOfBrokenList) == 1 and nbrOfBrokenList[0] == currentBrokenInRow):
            # print('This works')
            return 1
        else:
            return 0
    if currentBrokenInRow > nbrOfBrokenList[0]:
        return 0
    
    val = str[0]
    dontDoBroken = False
    dontDoWorking = False
    if currentBrokenInRow == nbrOfBrokenList[0]:
        if val[0] == '#':
            # print('Nope')
            return 0
        elif val[0] == '?':
            dontDoBroken = True

        nbrOfBrokenList.pop(0)
        currentBrokenInRow = 0
        if len(nbrOfBrokenList) == 0:
            if str.find('#') > -1:
                return 0
            else:
                # print('This also works')
                return 1
    elif currentBrokenInRow != 0 and currentBrokenInRow < nbrOfBrokenList[0]:
        dontDoWorking = True

    
    # print('current', currentBrokenInRow, nbrOfBrokenList)
    nbrOfPossibilities = 0
    if val == '?':
        nbrOfBrokenList1 = nbrOfBrokenList.copy()
        nbrOfBrokenList2 = nbrOfBrokenList.copy()
        if not dontDoBroken: 
            nbrOfPossibilities += findBroken('#' + str[1:], nbrOfBrokenList1, currentBrokenInRow, oldStr)
        if not dontDoWorking:
            nbrOfPossibilities += findBroken('.' + str[1:], nbrOfBrokenList2, currentBrokenInRow, oldStr)
    elif val == '#':
        if dontDoBroken:
            return 0
        currentBrokenInRow += 1
        nbrOfPossibilities += findBroken(str[1:], nbrOfBrokenList.copy(), currentBrokenInRow, oldStr + str[0])
    elif val == '.':
        if dontDoWorking:
            return 0
        currentBrokenInRow = 0
        nbrOfPossibilities += findBroken(str[1:], nbrOfBrokenList.copy(), currentBrokenInRow, oldStr + str[0])
    return nbrOfPossibilities

nbrOfPossibilities = 0
for line in lines:
    values = line.split(' ')
    puzzle = values[0]
    nbrOfBroken = values[1].split(',')
    nbrOfBroken = list(map(lambda v: int(v), nbrOfBroken))
    currentBrokenInRow = 0
    currentBrokenTotal = 0
    currentBrokenStreak = int(nbrOfBroken[0])
    totalBroken = sum(nbrOfBroken)
    
    alreadyBroken = [m.start() for m in re.finditer('#', line)]
    totalBrokenMissing = totalBroken - len(alreadyBroken)
    
    nbrOfPossibilities += findBroken(puzzle, nbrOfBroken, 0, '')
        
        
print(nbrOfPossibilities)