from collections import defaultdict

with open('5/input.txt') as f:
    lines = f.read().splitlines()

seeds = lines[0].split(':')[1].strip().split(' ')

maps = defaultdict(dict)


locations = list()

for seed in seeds:
    value = int(seed)
    hasTransformed = False
    mapIndex = 0
    for index, line in enumerate(lines[2:]):
        if line != '' and not line[0].isdigit():
            # print(mapIndex)
            hasTransformed = False
            mapIndex += 1
        elif not hasTransformed and line != '':
            # print('nummerrad')
            numbers = line.split(' ')
            dest = int(numbers[0])
            source = int(numbers[1])
            ran = int(numbers[2])
            if value >= source and value <= source + ran:
                # print(numbers, value)
                if dest > source:
                    value += dest - source
                else:
                    value -= source - dest
                hasTransformed = True
                # print(value)
        elif line == '' and not hasTransformed:
            # print('hittade ingen')
            hasTransformed = True
            
                

    locations.append(value)



locations.sort()
print(locations[0])
