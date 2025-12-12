import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

allInd = set()
for row in range(len(lines)):
    line = lines[row]
    for col in range(len(line)):
        if lines[row][col] == "@":
            allInd.add((row,col))

oldTot = -1
tot = 0
while oldTot != tot:
    oldTot = tot
    for row in range(len(lines)):
        line = lines[row]
        for col in range(len(line)):
            if (row,col) in allInd:
                nes = 0 
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if i == 0 and j == 0:
                            continue
                        if (row+i,col+j) in allInd:
                            nes += 1
                if nes < 4:
                    #print(row,col)
                    allInd.remove((row,col))
                    tot += 1

print(tot)
