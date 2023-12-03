with open('17/testInput.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 

movement = lines[0]
length = len(movement)
movementIndex = 0

room = [[1,1,1,1,1,1,1], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
currentMax = 0

def overlaps(rock, room):
    for x in range(0,len(rock)):
        for y in range(0,len(rock[0])):
            if rock[x][y] == 1 and room[x][y] == 1:
                return True
    return False


def merge(room, rock):
    for x in range(0,len(rock)):
        for y in range(0,len(rock[0])):
            if rock[x][y] == 1 or room[x][y] == 1:
                room[x][y] = 1


def newLine():
    l = [0,0,0,0,0,0,0]
    room.append(l)

for i in range(0,10):
    y = currentMax + 4
    falling = True

    if i%5 == 0:
        rock = [0,0,1,1,1,1,0]
        while falling:
            move = movement[movementIndex%length]
            if move == '<':
                if rock[0] != 1:
                    rock.pop(0)
                    rock.append(0)
                    if overlaps([rock], [room[y]]):
                        rock.pop()
                        rock.insert(0, 0)
            else:
                if rock[-1] != 1:
                    rock.pop()
                    rock.insert(0,0)
                    if overlaps([rock], [room[y]]):
                        rock.pop(0)
                        rock.append(0)
            if not overlaps([rock], [room[y-1]]):
                y -= 1
            else:
                merge([room[y]], [rock])
                if y > currentMax:
                    currentMax = y
                    newLine()
                falling = False

            movementIndex += 1
    
    if i%5 == 1:
        rock = [[0,0,0,1,0,0,0], [0,0,1,1,1,0,0], [0,0,0,1,0,0,0]]
        while falling:
            move = movement[movementIndex%length]
            if move == '<':
                if rock[1][0] != 1:
                    rock[0].pop(0)
                    rock[0].append(0)
                    rock[1].pop(0)
                    rock[1].append(0)
                    rock[2].pop(0)
                    rock[2].append(0)
                    if overlaps(rock, [room[y], room[y+1], room[y+2]]):
                        rock[0].pop()
                        rock[0].insert(0,0)
                        rock[1].pop()
                        rock[1].insert(0,0)
                        rock[2].pop()
                        rock[2].insert(0,0)
            else:
                if rock[1][-1] != 1:
                    rock[0].pop()
                    rock[0].insert(0,0)
                    rock[1].pop()
                    rock[1].insert(0,0)
                    rock[2].pop()
                    rock[2].insert(0,0)
                    if overlaps(rock, [room[y], room[y+1], room[y+2]]):
                        rock[0].pop(0)
                        rock[0].append(0)
                        rock[1].pop(0)
                        rock[1].append(0)
                        rock[2].pop(0)
                        rock[2].append(0)

            if not overlaps(rock, [room[y-1], room[y], room[y+1]]):
                y -= 1
            else:
                merge([room[y], room[y+1], room[y+2]], rock)
                if y+2 > currentMax:
                    currentMax = y+2
                    newLine()
                    newLine()
                    newLine()
                falling = False

            movementIndex += 1

    if i%5 == 2:
        rock = [[0,0,1,1,1,0,0], [0,0,0,0,1,0,0], [0,0,0,0,1,0,0]]
        while falling:
            move = movement[movementIndex%length]
            if move == '<':
                if rock[0][0] != 1:
                    rock[0].pop(0)
                    rock[0].append(0)
                    rock[1].pop(0)
                    rock[1].append(0)
                    rock[2].pop(0)
                    rock[2].append(0)
                    if overlaps(rock, [room[y], room[y+1], room[y+2]]):
                        rock[0].pop()
                        rock[0].insert(0,0)
                        rock[1].pop()
                        rock[1].insert(0,0)
                        rock[2].pop()
                        rock[2].insert(0,0)
            else:
                if rock[0][-1] != 1:
                    rock[0].pop()
                    rock[0].insert(0,0)
                    rock[1].pop()
                    rock[1].insert(0,0)
                    rock[2].pop()
                    rock[2].insert(0,0)
                    if overlaps(rock, [room[y], room[y+1], room[y+2]]):
                        rock[0].pop(0)
                        rock[0].append(0)
                        rock[1].pop(0)
                        rock[1].append(0)
                        rock[2].pop(0)
                        rock[2].append(0)

            if not overlaps(rock, [room[y-1], room[y], room[y+1]]):
                y -= 1
            else:
                merge([room[y], room[y+1], room[y+2]], rock)
                if y+2 > currentMax:
                    currentMax = y+2
                    newLine()
                    newLine()
                    newLine()
                falling = False

            movementIndex += 1
    
    if i%5 == 3:
        rock = [[0,0,1,0,0,0,0], [0,0,1,0,0,0,0], [0,0,1,0,0,0,0], [0,0,1,0,0,0,0]]
        while falling:
            move = movement[movementIndex%length]
            if move == '<':
                if rock[2][0] != 1:
                    rock[0].pop(0)
                    rock[0].append(0)
                    rock[1].pop(0)
                    rock[1].append(0)
                    rock[2].pop(0)
                    rock[2].append(0)
                    rock[3].pop(0)
                    rock[3].append(0)
                    if overlaps(rock, [room[y], room[y+1], room[y+2], room[y+3]]):
                        rock[0].pop()
                        rock[0].insert(0,0)
                        rock[1].pop()
                        rock[1].insert(0,0)
                        rock[2].pop()
                        rock[2].insert(0,0)
                        rock[3].pop()
                        rock[3].insert(0,0)
            else:
                if rock[0][-1] != 1:
                    rock[0].pop()
                    rock[0].insert(0,0)
                    rock[1].pop()
                    rock[1].insert(0,0)
                    rock[2].pop()
                    rock[2].insert(0,0)
                    rock[3].pop()
                    rock[3].insert(0,0)
                    if overlaps(rock, [room[y], room[y+1], room[y+2], room[y+3]]):
                        rock[0].pop(0)
                        rock[0].append(0)
                        rock[1].pop(0)
                        rock[1].append(0)
                        rock[2].pop(0)
                        rock[2].append(0)
                        rock[3].pop(0)
                        rock[3].append(0)

            if not overlaps(rock, [room[y-1], room[y], room[y+1], room[y+2]]):
                y -= 1
            else:
                merge([room[y], room[y+1], room[y+2], room[y+3]], rock)
                if y+3 > currentMax:
                    currentMax = y+3
                    newLine()
                    newLine()
                    newLine()
                    newLine()
                falling = False

            movementIndex += 1
    
    if i%5 == 4:
        rock = [[0,0,1,1,0,0,0], [0,0,1,1,0,0,0]]
        while falling:
            move = movement[movementIndex%length]
            if move == '<':
                if rock[0][0] != 1:
                    rock[0].pop(0)
                    rock[0].append(0)
                    rock[1].pop(0)
                    rock[1].append(0)
                    if overlaps(rock, [room[y], room[y+1]]):
                        rock[0].pop()
                        rock[0].insert(0,0)
                        rock[1].pop()
                        rock[1].insert(0,0)
            else:
                if rock[0][-1] != 1:
                    rock[0].pop()
                    rock[0].insert(0,0)
                    rock[1].pop()
                    rock[1].insert(0,0)
                    if overlaps(rock, [room[y], room[y+1]]):
                        rock[0].pop(0)
                        rock[0].append(0)
                        rock[1].pop(0)
                        rock[1].append(0)

            if not overlaps(rock, [room[y-1], room[y]]):
                y -= 1
            else:
                merge([room[y], room[y+1]], rock)
                if y+1 > currentMax:
                    currentMax = y+1
                    newLine()
                    newLine()
                falling = False

            movementIndex += 1

# for row in range(len(room)-1, 0, -1):
#     print(room[row])
print(currentMax)