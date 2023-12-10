with open('9/input.txt') as f:
    lines = f.read().splitlines()

totalSum = 0
for line in lines:
    line = line.split(' ')
    newLine = []
    totalSum += int(line[-1])
    while(True):
        for i in range(1,len(line)):
            newLine.append(int(line[i]) - int(line[i-1]))
        if newLine.count(0) == len(newLine):
            break
        else:
            totalSum += newLine[-1]
            line = newLine
            newLine = []

print(totalSum)