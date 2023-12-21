from queue import Queue
with open('21/input.txt') as f:
    lines = f.read().splitlines()

garden = dict()
startPos = (0,0)

for row, line in enumerate(lines):
    for col in range(0,len(line)):
        if line[col] == 'S':
            startPos = (row, col, 0)
            garden[(row,col)] = '.'
        else:
            garden[(row,col)] = line[col]

steps = Queue()
steps.put(startPos)
evensteps = dict()
oddsteps = dict()

while not steps.empty():
    pos = steps.get()
    # print(pos)
    row = pos[0]
    col = pos[1]
    nbr = pos[2]
    goNext = True
    if nbr % 2 == 0:
        if (row, col) not in evensteps:
            evensteps[(row, col)] = True
        else:
            goNext = False
    else:
        if (row, col) not in oddsteps:
            oddsteps[(row, col)] = True
        else:
            goNext = False
    # else:

    if goNext:
        newNbr = nbr + 1
        if newNbr <= 64:
            if (row+1, col) in garden and garden[(row+1, col)] != '#' and (row+1, col) not in evensteps:
                steps.put((row+1, col, newNbr))
            if (row-1, col) in garden and garden[(row-1, col)] != '#' and (row-1, col) not in evensteps:
                steps.put((row-1, col, newNbr))
            if (row, col+1) in garden and garden[(row, col+1)] != '#' and (row, col+1) not in evensteps:
                steps.put((row, col+1, newNbr))
            if (row, col-1) in garden and garden[(row, col-1)] != '#' and (row, col-1) not in evensteps:
                steps.put((row, col-1, newNbr))

print(len(evensteps))