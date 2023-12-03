with open('14/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 

cave = dict()
maximalY = 0
maximalX = 0
minimalX = 1000

for line in lines:
    elems = line.split('->')
    elem1 = elems[0]
    for i in range(1, len(elems)):
        elem2 = elems[i]
        coord1 = elem1.split(',')
        coord2 = elem2.split(',')
        maxX = max(int(coord1[0]), int(coord2[0]))
        maxY = max(int(coord1[1]), int(coord2[1]))
        minX = min(int(coord1[0]), int(coord2[0]))
        minY = min(int(coord1[1]), int(coord2[1]))
        for j in range(minX, maxX+1):
            for k in range(minY, maxY+1):
                if k > maximalY:
                    maximalY = k
                if j < minimalX:
                    minimalX = j
                if j > maximalX:
                    maximalX = j
                cave[(j,k)] = '#'
        elem1 = elem2

for j in range(minimalX-10000, maximalX+10000):
    cave[(j,maximalY+2)] = '#'

sandUnits = 0
moreSand = True
sandX = 500
sandY =  0
while moreSand:
    if (sandX, sandY+1) not in cave:
        sandY += 1
    elif (sandX-1, sandY+1) not in cave:
        sandX -= 1
        sandY += 1
    elif (sandX+1, sandY+1) not in cave:
        sandX += 1
        sandY += 1
    else:
        cave[(sandX, sandY)] = 'o'
        if (sandX, sandY) == (500, 0):
            moreSand = False
        sandUnits += 1
        sandX = 500
        sandY = 0

print(sandUnits)