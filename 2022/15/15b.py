with open('15/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 

m = dict()
possible = set()
sensors = dict()

maxVal = 4000000
for line in lines:
    words = line.split(' ')
    x = int(words[2][2:-1])
    y = int(words[3][2:-1])
    beaconX = int(words[8][2:-1])
    beaconY = int(words[9][2:])
    manhattan = abs(x-beaconX) + abs(y-beaconY)
    sensors[(x, y)] = manhattan
    candidateDistance = manhattan+1
    for i in range(-1*(candidateDistance), candidateDistance+1):
        if(x+i >= 0 and x+i <= maxVal):
            j = -1*(candidateDistance - abs(i))
            if y+j >= 0 and y+j <= maxVal:
                possible.add((x+i, y+j))
            if y-j >= 0 and y-j <= maxVal:
                possible.add((x+i, y-j))

print(len(possible))
for x, y in possible:
    theOne = True
    for sensor, manhattan in sensors.items():
        sensorX = sensor[0]
        sensorY = sensor[1]
        if abs(sensorX-x)+abs(sensorY-y) <= manhattan:
            theOne = False
            break
    if theOne:
        print(x*4000000+y)
        break