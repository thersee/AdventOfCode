import sys
from queue import PriorityQueue
from functools import cmp_to_key

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

points = set()
prev = lines[-1].split(',')
prev = [int(prev[0]), int(prev[1])]
minCol = maxCol = int(prev[0])
minRow = maxRow = int(prev[1])
outline = set()

for line in lines:
    curr = line.split(',')
    curr = [int(curr[0]), int(curr[1])]
    for col in range(min(int(prev[0]), int(curr[0])), max(int(prev[0]), int(curr[0]))+1):
        for row in range(min(int(prev[1]), int(curr[1])), max(int(prev[1]), int(curr[1]))+1):
            #print(col,row)
            points.add((col,row))
            if prev[0] == curr[0]:
                if prev[1]>curr[1]:
                    outline.add((col-1,row))
                    #print(col-1,row)
                else:
                    outline.add((col+1,row))
                    #print(col+1,row)
            else:
                if prev[0] > curr[0]:
                    outline.add((col, row+1))
                    #print(col,row+1)
                else:
                    outline.add((col, row-1))
                    #print(col,row-1)

            
            if col < minCol:
                minCol = col
            if col > maxCol:
                maxCol = col
            if row < minRow:
                minRow = row
            if row > maxRow:
                maxRow = row
    prev = curr
    #print("#"*50)

intersection = outline.intersection(points)
outline = outline.difference(intersection)
#print(len(outline))


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

done = False
for area in areas:
    print(area)
    if done:
        break
    line1 = area[1][0]
    line2 = area[1][1]
    x1,y1 = line1.split(',')
    x2,y2 = line2.split(',')
    #print(x1,y1,x2,y2)

    try:
        for col in range(min(int(x1), int(x2)), max(int(x1), int(x2))+1):
            if (col,int(y1)) in outline or (col,int(y2))in outline:
                raise "no"
        for row in range(min(int(y1), int(y2)), max(int(y1), int(y2))+1):
                
            if (int(x1),row) in outline or (int(x2),row) in outline:
                #print(col,row, "visited")
                raise "no"
        maxArea = area
        done = True
    except:
        continue
print(maxArea)

'''
maxArea = 0
for i in range(0, len(lines)):
    line1 = lines[i]
    print("new corner", line1)
    for j in range(i, len(lines)):
        line2 = lines[j]
        if line1 != line2:
            #print("#"*50)
            #print(line1,line2)
            x1,y1 = line1.split(',')
            x2,y2 = line2.split(',')
            #print(x1,y1,x2,y2)
            area = (abs((int(x1)-int(x2)))+1)*(abs((int(y1)-int(y2)))+1)
            #print(area)
            if area > maxArea:
                #print("bigger")
                try:
                    for col in range(min(int(x1), int(x2)), max(int(x1), int(x2))+1):
                        if (col,int(y1)) in outline or (col,int(y2))in outline:
                            raise "no"
                    for row in range(min(int(y1), int(y2)), max(int(y1), int(y2))+1):
                            
                        if (int(x1),row) in outline or (int(x2),row) in outline:
                            #print(col,row, "visited")
                            raise "no"
                    maxArea = area
                except:
                    continue

print(maxArea)





""" rim = set()
visited = set()
q = PriorityQueue()

q.put((minCol-1,minRow-1))
while q.qsize() > 0:
    
    col, row = q.get()
    #print(col, row)
    if col < minCol-1 or col > maxCol+1:
        continue
    if row < minRow -1 or row > maxRow +1:
        continue
    if (col,row) in visited:
        continue
    if (col,row) in points:
        continue
    visited.add((col,row))
    if len(visited) % 10000 == 0:
        print(len(visited))
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            q.put((col+i, row+j))
      

#print(visited)

maxArea = 0
for i in range(0, len(lines)):
    line1 = lines[i]
    for j in range(i, len(lines)):
        line2 = lines[j]
        if line1 != line2:
            #print("#"*50)
            #print(line1,line2)
            x1,y1 = line1.split(',')
            x2,y2 = line2.split(',')
            #print(x1,y1,x2,y2)
            area = (abs((int(x1)-int(x2)))+1)*(abs((int(y1)-int(y2)))+1)
            #print(area)
            if area > maxArea:
                #print("bigger")
                try:
                    for col in range(min(int(x1), int(x2)), max(int(x1), int(x2))+1):
                        for row in range(min(int(y1), int(y2)), max(int(y1), int(y2))+1):
                            #print(col,row)
                            if (col,row) in visited:
                                #print(col,row, "visited")
                                raise "no"
                    maxArea = area
                except:
                    continue
                   

            #print(x1,y1,x2,y2,area)


print(maxArea)
 """
       '''