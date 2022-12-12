#464 fel, too high

with open('12/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 

x = -1
y = -1

goalX = -1
goalY = -1

visited = dict()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if lines[i][j] == 'S':
            lines[i]= lines[i].replace('S','a')
        elif lines[i][j] == 'E':
            x = i
            y = j
            lines[i]=lines[i].replace('E','z')


toVisit = [(x,y)]
visited = dict()
visited[(x,y)] = 0

while toVisit:
    x,y = toVisit.pop(0)
    currLen = visited[(x,y)]
    print(lines[x][y])
    if lines[x][y] == 'a':
        break
    
    if x-1 >= 0 and alpha.find(lines[x-1][y])+1 >= alpha.find(lines[x][y]):
        if (x-1, y) not in visited:
            visited[(x-1,y)] = currLen+1
            toVisit.append((x-1, y))
        elif visited[(x-1,y)] > currLen+1:
            print('hej')
            visited[(x-1,y)] = currLen+1
            toVisit.append((x-1, y))


    if x+1 < len(lines) and alpha.find(lines[x+1][y])+1 >= alpha.find(lines[x][y]):
        if (x+1, y) not in visited:
            visited[(x+1,y)] = currLen+1
            toVisit.append((x+1, y))
        elif visited[(x+1,y)] > currLen+1:
            print('hej')
            visited[(x+1,y)] = currLen+1
            toVisit.append((x+1, y))

    
    if y-1 >= 0 and alpha.find(lines[x][y-1])+1 >= alpha.find(lines[x][y]):
        if (x, y-1) not in visited:
            visited[(x,y-1)] = currLen+1
            toVisit.append((x, y-1))
        elif visited[(x,y-1)] > currLen+1:
            print('hej')
            visited[(x,y-1)] = currLen+1
            toVisit.append((x, y-1))

    if y+1 < len(lines[0]) and alpha.find(lines[x][y+1])+1 >= alpha.find(lines[x][y]):
        if (x, y+1) not in visited:
            visited[(x,y+1)] = currLen+1
            toVisit.append((x, y+1))
        elif visited[(x,y+1)] > currLen+1:
            print('hej')
            visited[(x,y+1)] = currLen+1
            toVisit.append((x, y+1))
    print(toVisit)

print(currLen)
print(x,y)

        