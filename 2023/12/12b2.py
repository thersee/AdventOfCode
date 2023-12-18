from functools import cache

with open('12/input.txt') as f:
    lines = f.read().splitlines()

@cache
def findBroken(inputString):
    inp = inputString.split(', ')
    str1 = inp[0][2:-1]
    nbrOfBrokenList = list()
    for i in inp[1:-1]:
        i =i.strip('[')
        i = i.strip(']')
        nbrOfBrokenList.append(int(i))
    currentBrokenInRow = int(inp[-1][:-1])
    if (len(str1) == 0):
        if len(nbrOfBrokenList) == 0 or (len(nbrOfBrokenList) == 1 and nbrOfBrokenList[0] == currentBrokenInRow):
            # print('This works')
            return 1
        else:
            return 0
    if currentBrokenInRow > nbrOfBrokenList[0]:
        return 0
    
    val = str1[0]
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
            if str1.find('#') > -1:
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
            nbrOfPossibilities += findBroken(str(('#' + str1[1:], nbrOfBrokenList1, currentBrokenInRow)))
        if not dontDoWorking:
            nbrOfPossibilities += findBroken(str(('.' + str1[1:], nbrOfBrokenList2, currentBrokenInRow)))
    elif val == '#':
        if dontDoBroken:
            return 0
        currentBrokenInRow += 1
        nbrOfPossibilities += findBroken(str((str1[1:], nbrOfBrokenList.copy(), currentBrokenInRow)))
    elif val == '.':
        if dontDoWorking:
            return 0
        currentBrokenInRow = 0
        nbrOfPossibilities += findBroken(str((str1[1:], nbrOfBrokenList.copy(), currentBrokenInRow)))
    return nbrOfPossibilities

nbrOfPossibilities = 0
for line in lines:
    values = line.split(' ')
    puzzle = values[0]
    puzzle = '?'.join([puzzle]*5)
    nbrOfBroken = values[1].split(',')*5
    nbrOfBroken = list(map(lambda v: int(v), nbrOfBroken))
    currentBrokenInRow = 0
    currentBrokenTotal = 0
    currentBrokenStreak = int(nbrOfBroken[0])
    totalBroken = sum(nbrOfBroken)
    
    nbrOfPossibilities += findBroken(str((puzzle, nbrOfBroken, 0)))
        
        
print(nbrOfPossibilities)