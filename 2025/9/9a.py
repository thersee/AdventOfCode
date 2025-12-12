import sys
from queue import PriorityQueue
from functools import cmp_to_key

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

areas = list()
for i in range(0, len(lines)):
    line1 = lines[i]
    for j in range(i, len(lines)):
        line2 = lines[j]
        if line1 != line2:
            x1,y1 = line1.split(',')
            x2,y2 = line2.split(',')
            #print(x1,y1,x2,y2)
            area = (abs((int(x1)-int(x2)))+1)*(abs((int(y1)-int(y2)))+1)
            #print(x1,y1,x2,y2,area)
            areas.append((area, (line1, line2)))

areas.sort(reverse=True)
print(areas[0])