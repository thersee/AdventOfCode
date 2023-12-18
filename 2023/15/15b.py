with open('15/input.txt') as f:
    lines = f.read().splitlines()

line = lines[0]
values = line.split(',')

boxes = [[] for i in range(0,256)]

for value in values:
    if '-' in value:
        parts = value.split('-')
        thisSum = 0
        for c in range(0, len(parts[0])):
            thisSum += ord(parts[0][c])
            thisSum *= 17
            thisSum = thisSum % 256
        lenses = boxes[thisSum]
        indexToRemove = -1
        for index, lens in enumerate(lenses):
            if parts[0] in lens:
                indexToRemove = index
                break
        if indexToRemove > -1:
            del lenses[indexToRemove]
    elif '=' in value:
        parts = value.split('=')
        thisSum = 0
        for c in range(0, len(parts[0])):
            thisSum += ord(parts[0][c])
            thisSum *= 17
            thisSum = thisSum % 256

        lenses = boxes[thisSum]
        indexToReplace = -1
        for index, lens in enumerate(lenses):
            if parts[0] in lens:
                indexToReplace = index
                break
        if indexToReplace > -1:
            lenses[indexToReplace] = value
        else:
            lenses.append(value)

totalPower = 0
for boxIndex, box in enumerate(boxes):
    for lensIndex, lens in enumerate(box):
        totalPower += (boxIndex+1)*(lensIndex+1)*int(lens.split('=')[-1])

print(totalPower)
