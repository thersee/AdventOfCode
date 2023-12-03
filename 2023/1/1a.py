
with open('1/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines]


sum = 0
for i in range(0, len(lines)):
    firstDigit = -1
    lastDigit = -1
    line = lines[i]
    for j in range(0, len(line)): 
        if(firstDigit == -1 and line[j].isdigit()):
            firstDigit = line[j]
        if(lastDigit == -1 and line[len(line) -1 -j].isdigit()):
            lastDigit = line[len(line) -1 -j]
        if(firstDigit != -1 and lastDigit != -1):
            sum = sum + int(firstDigit+lastDigit)
            break

    

print(sum)
