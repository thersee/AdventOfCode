with open('13/input.txt') as f:
    lines = f.read().splitlines()

def almostEqual(l1, l2, alreadyAdjusted):
    if alreadyAdjusted:
        return False
    nbrOfUnequal = 0
    for i in range(0,len(l1)):
        if l1[i] != l2[i]:
            nbrOfUnequal += 1
            if nbrOfUnequal > 1:
                return False
    return nbrOfUnequal == 1

def equal(l, start, stop, alreadyAdjusted):
    # print(l[start], l[stop])
    almost = almostEqual(l[start], l[stop], alreadyAdjusted)
    if l[start] != l[stop] and not almost:
        # print('olika')
        return False
    else:
        if start > 0 and stop < len(l) -1:
            isAdjusted = alreadyAdjusted or almost
            # print(alreadyAdjusted, almost, isAdjusted)
            return equal(l, start -1, stop +1, isAdjusted)
        else: 
            # print(start, stop, l)
            if alreadyAdjusted or almost:
                return True
            else:
                return False

totalSum = 0
allRows = list()
allCols = ['' for i in range(len(lines[0]))]
for i, line in enumerate(lines):
    # print(line)
    if line != '':
        allRows.append(line)
        for index, c in enumerate(line):
            allCols[index] += c
    else:
        # print(allRows)
        alreadyFound = False
        for index in range(1, len(allRows)):
            if equal(allRows, index-1, index, False):
                alreadyFound = True
                totalSum += 100*(index)
                break
        if not alreadyFound:
            for index in range(1, len(allCols)):
                if equal(allCols, index-1, index, False):
                    totalSum += index
        if i != len(lines)-1:
            allRows = list()
            allCols = ['' for i in range(len(lines[i+1]))]
    
    #37779 too low
print(totalSum)