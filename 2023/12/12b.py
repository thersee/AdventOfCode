import re

with open('12/inputTest.txt') as f:
    lines = f.read().splitlines()

oldAnswers = dict()


def findBroken(str1, 
                nbrOfBrokenList, 
                currentBrokenInRow):
    # print(oldStr, str)
    if (len(str1) == 0):
        if len(nbrOfBrokenList) == 0 or (len(nbrOfBrokenList) == 1 and nbrOfBrokenList[0] == currentBrokenInRow):
            # print('This works')
            oldAnswers[str((str1, nbrOfBroken, currentBrokenInRow))] = 1
            return 1
        else:
            oldAnswers[str((str1, nbrOfBroken, currentBrokenInRow))] = 0
            return 0
    if currentBrokenInRow > nbrOfBrokenList[0]:
        oldAnswers[str((str1, nbrOfBroken, currentBrokenInRow))] = 0
        return 0
    
    val = str1[0]
    dontDoBroken = False
    dontDoWorking = False
    if currentBrokenInRow == nbrOfBrokenList[0]:
        if val[0] == '#':
            # print('Nope')
            oldAnswers[str((str1, nbrOfBroken, currentBrokenInRow))] = 0
            return 0
        elif val[0] == '?':
            dontDoBroken = True

        nbrOfBrokenList.pop(0)
        currentBrokenInRow = 0
        if len(nbrOfBrokenList) == 0:
            if str1.find('#') > -1:
                oldAnswers[str((str1, nbrOfBroken, currentBrokenInRow))] = 0
                return 0
            else:
                oldAnswers[str((str1, nbrOfBroken, currentBrokenInRow))] = 1
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
            if str(('#' + str1[1:], nbrOfBrokenList1, currentBrokenInRow)) in oldAnswers:
                print('yes')
                nbrOfPossibilities += oldAnswers[str(('#' + str1[1:], nbrOfBrokenList1, currentBrokenInRow))]
            else:
                nbrOfPossibilities += findBroken('#' + str1[1:], nbrOfBrokenList1, currentBrokenInRow)
        if not dontDoWorking:
            if str(('.' + str1[1:], nbrOfBrokenList2, currentBrokenInRow)) in oldAnswers:
                print('yes')
                nbrOfPossibilities += oldAnswers[str(('.' + str1[1:], nbrOfBrokenList2, currentBrokenInRow))]
            else:
                nbrOfPossibilities += findBroken('.' + str1[1:], nbrOfBrokenList2, currentBrokenInRow)
    elif val == '#':
        if dontDoBroken:
            return 0
        currentBrokenInRow += 1
        nbrOfBrokenList3 = nbrOfBrokenList.copy()
        if str((str1[1:], nbrOfBrokenList3, currentBrokenInRow)) in oldAnswers:
            print('yes')
            nbrOfPossibilities += oldAnswers[str((str1[1:], nbrOfBrokenList3, currentBrokenInRow))]
        else:
            nbrOfPossibilities += findBroken(str1[1:], nbrOfBrokenList3, currentBrokenInRow)
    elif val == '.':
        if dontDoWorking:
            return 0
        currentBrokenInRow = 0
        nbrOfBrokenList4 = nbrOfBrokenList.copy()
        if str((str1[1:], nbrOfBrokenList4, currentBrokenInRow)) in oldAnswers:
            print('yes')
            nbrOfPossibilities += oldAnswers[str((str1[1:], nbrOfBrokenList4, currentBrokenInRow))]
        else:
            nbrOfPossibilities += findBroken(str1[1:], nbrOfBrokenList4, currentBrokenInRow)
    
    oldAnswers[str((str1, nbrOfBroken, currentBrokenInRow))] = nbrOfPossibilities
    return nbrOfPossibilities

nbrOfPossibilities = 0
for index, line in enumerate(lines):
    values = line.split(' ')
    puzzle = values[0]
    puzzle = '?'.join([puzzle]*5)
    nbrOfBroken = values[1].split(',')*5
    nbrOfBroken = list(map(lambda v: int(v), nbrOfBroken))
    currentBrokenInRow = 0
    currentBrokenTotal = 0
    currentBrokenStreak = int(nbrOfBroken[0])
    totalBroken = sum(nbrOfBroken)
    
    alreadyBroken = [m.start() for m in re.finditer('#', line)]
    totalBrokenMissing = totalBroken - len(alreadyBroken)
    
    nbrOfPossibilities += findBroken(puzzle, nbrOfBroken, 0)
    print(len(oldAnswers.keys()))
    print(index, line)
        
        
print(nbrOfPossibilities)