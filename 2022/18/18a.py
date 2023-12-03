with open('18/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 


exposed = dict()
for line in lines:
    line = line.split(',')
    x = int(line[0])
    y = int(line[1])
    z = int(line[2])
    e = 0
    if (x-1, y, z) not in exposed:
        e += 1
    else:
        exposed[(x-1, y, z)] -= 1
    if (x+1, y, z) not in exposed:
        e += 1
    else:
        exposed[(x+1, y, z)] -= 1

    if (x, y-1, z) not in exposed:
        e += 1
    else:
        exposed[(x, y-1, z)] -= 1
    if (x, y+1, z) not in exposed:
        e += 1
    else:
        exposed[(x, y+1, z)] -= 1

    if (x, y, z-1) not in exposed:
        e += 1
    else:
        exposed[(x, y, z-1)] -= 1
    if (x, y, z+1) not in exposed:
        e += 1
    else:
        exposed[(x, y, z+1)] -= 1



    exposed[(x,y,z)] = e

total = 0
for k, val in exposed.items():
    total += val

print(total)