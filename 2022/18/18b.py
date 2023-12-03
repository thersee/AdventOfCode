allValues = set()
with open('18/input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    line = line.split(',')
    x = int(line[0])
    y = int(line[1])
    z = int(line[2])
    allValues.add((x,y,z))


outerExposed = set()
innerExposed = set()
numberExposed = 0

def checkSide(point):
    global allValues
    global outerExposed
    global innerExposed
    global numberExposed

    if point in outerExposed:
        numberExposed += 1
        return

    if point not in allValues:
        toCheck = [point]
        alreadyChecked = set()
        isInner = True
        while toCheck:
            side = toCheck.pop(0)
            if side[0] > 20 or side[0] <0 or side[1] > 20 or side[1] <0 or side[2] > 20 or side[2] <0:
                numberExposed += 1
                outerExposed = outerExposed.union(alreadyChecked)
                isInner = False
                return
            if (side[0]-1, side[1], side[2]) not in allValues and (side[0]-1, side[1], side[2]) not in alreadyChecked:

                alreadyChecked.add((side[0]-1, side[1], side[2]))
                toCheck.append((side[0]-1, side[1], side[2]))

            if (side[0]+1, side[1], side[2]) not in allValues and (side[0]+1, side[1], side[2]) not in alreadyChecked:

                alreadyChecked.add((side[0]+1, side[1], side[2]))
                toCheck.append((side[0]+1, side[1], side[2]))

            if (side[0], side[1]-1, side[2]) not in allValues and (side[0], side[1]-1, side[2]) not in alreadyChecked:
                alreadyChecked.add((side[0], side[1]-1, side[2]))
                toCheck.append((side[0], side[1]-1, side[2]))
            
            if (side[0], side[1]+1, side[2]) not in allValues and (side[0], side[1]+1, side[2]) not in alreadyChecked:
                alreadyChecked.add((side[0], side[1]+1, side[2]))
                toCheck.append((side[0], side[1]+1, side[2]))
            
            if (side[0], side[1], side[2]-1) not in allValues and (side[0], side[1], side[2]-1) not in alreadyChecked:
                alreadyChecked.add((side[0], side[1], side[2]-1))
                toCheck.append((side[0], side[1], side[2]-1))
            
            if (side[0], side[1], side[2]+1) not in allValues and (side[0], side[1], side[2]+1) not in alreadyChecked:
                alreadyChecked.add((side[0], side[1], side[2]+1))
                toCheck.append((side[0], side[1], side[2]+1))

        if isInner:
            innerExposed = innerExposed.union(alreadyChecked)
            innerExposed.add(point)

for value in lines:
    value = value.split(',')
    x = int(value[0])
    y = int(value[1])
    z = int(value[2])

    checkSide((x-1,y,z))
    checkSide((x+1,y,z))
    checkSide((x,y-1,z))
    checkSide((x,y+1,z))
    checkSide((x,y,z-1))
    checkSide((x,y,z+1))

print(numberExposed)






