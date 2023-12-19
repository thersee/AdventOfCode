from queue import Queue

with open('18/input.txt') as f:
    lines = f.read().splitlines()

corners = list()
row = 0
col = 0
totalEdge = 0

# corners.append((row, col))
for line in lines:
    vals = line.split(' ')[2]
    dir = vals[-2:-1]
    num = int(vals[2:-2], 16)
    totalEdge += num
    # vals = line.split(' ')
    # dir = vals[0]
    # num = int(vals[1])
    if dir == '1':
    # if dir == 'D':
        row += num
        corners.append((row, col))
    elif dir == '3':
    # elif dir == 'U':
        row -= num

        corners.append((row, col))
    elif dir == '2':
    # elif dir == 'L':
        col -= num
        
        corners.append((row, col))
    elif dir == '0':
    # elif dir == 'R':
        col += num
        
        corners.append((row, col))

print(corners)
area = 0
corners = list(corners)
for i in range(0, len(corners)):
    x = corners[i]
    if i+1 == len(corners):
        i = -1
    y = corners[i+1]
    area += (x[0]*y[1] - x[1]*y[0])/2.


print(abs(area)+totalEdge/2.0+1)
# print(abs(area)+3168/2+1)
# print(area)
