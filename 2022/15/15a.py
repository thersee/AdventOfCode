with open('15/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 

m = dict()
row10 = set()
beacons = set()
for line in lines:
    words = line.split(' ')
    x = int(words[2][2:-1])
    y = int(words[3][2:-1])
    beaconX = int(words[8][2:-1])
    beaconY = int(words[9][2:])
    beacons.add((beaconX, beaconY))
    manhattan = abs(x-beaconX) + abs(y-beaconY)
    j = 2000000-y
    for i in range(-1*(manhattan-abs(j)), manhattan-abs(j)+1):
        row10.add((x+i, y+j))


print(len(row10-beacons))
#print(m)