
with open('1/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines]

maxNbr1 = 0
maxNbr2 = 0
maxNbr3 = 0
sumNow = 0
for i in range(0, len(lines)):
    if(lines[i] == ''):
        if (sumNow > maxNbr1):
            maxNbr3 = maxNbr2
            maxNbr2 = maxNbr1
            maxNbr1 = sumNow
        elif (sumNow > maxNbr2):
            maxNbr3 = maxNbr2
            maxNbr2 = sumNow
        elif (sumNow > maxNbr3):
            maxNbr3 = sumNow
        sumNow = 0
    else:
        sumNow += int(lines[i])
    

print(maxNbr1 + maxNbr2 + maxNbr3)
