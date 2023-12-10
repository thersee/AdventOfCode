from collections import defaultdict

with open('8/input.txt') as f:
    lines = f.read().splitlines()

instructions = lines[0].replace('L', '0').replace('R', '1')
# print(instructions)
way = defaultdict(tuple)
for line in lines[2:]:
    node, adjacent = line.split(' = (')
    left, right = adjacent.split(', ')
    way[node] = (left, right[0:-1])

# print(way)
nbrOfSteps = 0
nextStep = 0
currentPos = 'AAA'
while(currentPos != 'ZZZ'):
    currentPos = way[currentPos][int(instructions[nextStep])]
    nextStep += 1 
    nextStep = nextStep % len(instructions)
    nbrOfSteps += 1

print(nbrOfSteps)

