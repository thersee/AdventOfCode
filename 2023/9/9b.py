with open('9/input.txt') as f:
    lines = f.read().splitlines()

totalSum = 0
for line in lines:
    line = line.split(' ')
    newLine = []
    totalSum += int(line[0])
    nextMinus = True
    while(True):
        for i in range(1,len(line)):
            newLine.append(int(line[i]) - int(line[i-1]))
        if newLine.count(0) == len(newLine):
            break
        else:
            if nextMinus:
                totalSum -= newLine[0]
            else:
                totalSum += newLine[0]
            nextMinus = not nextMinus
            line = newLine
            newLine = []

print(totalSum)