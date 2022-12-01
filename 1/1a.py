
with open('1/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines]

maxNbr = 0
sumNow = 0
for i in range(0, len(lines)):
    if(lines[i] == ''):
        if sumNow > maxNbr:
            maxNbr = sumNow
        sumNow = 0;
    else:
        sumNow += int(lines[i])
    

print(maxNbr)
