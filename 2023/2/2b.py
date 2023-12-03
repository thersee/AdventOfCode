with open('2/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines]

totalSum = 0

for line in lines:
    frags = line.split(':')
    index = frags[0].split(' ')[1]
    revealed = frags[1].split(';')
    minRed = 0
    minGreen = 0
    minBlue = 0
    for r in revealed:
        cubes = r.split(',')
        for cube in cubes:
            cubeInfo = cube.split(' ')
            color = cubeInfo[2]
            number = int(cubeInfo[1])
            if color == 'red' and number > minRed:
                minRed = number
                
            if color == 'green' and number > minGreen:
                minGreen = number
                
            if color == 'blue' and number > minBlue:
                minBlue = number
                
    totalSum = totalSum + minRed*minBlue*minGreen

print(totalSum)