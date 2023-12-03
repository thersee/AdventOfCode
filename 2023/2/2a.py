with open('2/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines]

maxRed = 12
maxGreen = 13
maxBlue = 14
totalValid = 0

for line in lines:
    frags = line.split(':')
    index = frags[0].split(' ')[1]
    revealed = frags[1].split(';')
    valid = True
    for r in revealed:
        cubes = r.split(',')
        for cube in cubes:
            cubeInfo = cube.split(' ')
            color = cubeInfo[2]
            number = int(cubeInfo[1])
            if color == 'red' and number > maxRed:
                valid = False
                break
            if color == 'green' and number > maxGreen:
                valid = False
                break
            if color == 'blue' and number > maxBlue:
                valid = False
                break
    if valid:
        totalValid += int(index)

print(totalValid)