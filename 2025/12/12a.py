import sys
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

i = 0
shapes = list()
while i < 6*5:
    volume = 0
    for j in range(3):
        line=lines[i+j+1]
        for l in line:
            if l == '#':
                volume += 1
    shapes.append(volume)
    i += 5
print(shapes)

possible = 0
for k in range(i,len(lines)):
    line = lines[k]
    print(line)
    rect, values = line.split(': ')
    values = values.split(' ')
    sides = rect.split('x')
    totalArea = int(sides[0])*int(sides[1])
    area = 0
    for ind, v in enumerate(values):
        area += int(v)*shapes[ind]
    print(area, totalArea)
    if area < totalArea:
        possible += 1

print(possible)


