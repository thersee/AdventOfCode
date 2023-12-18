with open('13/input.txt') as f:
    lines = f.read().splitlines()

print(len(lines))
def equal(l, start, stop):
    if l[start] != l[stop]:
        return False
    else:
        if start > 0 and stop < len(l) -1:
            return equal(l, start -1, stop +1)
        else: 
            # print(start, stop, l)
            return True

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
        for index in range(1, len(allRows)):
            if equal(allRows, index-1, index):
                totalSum += 100*(index)
        for index in range(1, len(allCols)):
            if equal(allCols, index-1, index):
                totalSum += index
        if i != len(lines)-1:
            allRows = list()
            allCols = ['' for i in range(len(lines[i+1]))]
    
print(totalSum)