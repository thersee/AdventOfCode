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


possible = 0
totalLines = 0
impossible = 0
for k in range(i,len(lines)):
    totalLines += 1
    line = lines[k]
    rect, values = line.split(': ')
    values = values.split(' ')
    sides = rect.split('x')
    a = int(int(sides[0])/3)
    b = int(int(sides[1])/3)
    tot = 0
    for v in values:
        tot += int(v)
    if a*b >= tot:
        possible += 1

    totalArea = int(sides[0])*int(sides[1])
    area = 0
    for ind, v in enumerate(values):
        area += int(v)*shapes[ind]

    if area > totalArea:
        impossible += 1

print(possible, totalLines, impossible)

#472
