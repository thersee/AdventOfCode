from collections import defaultdict

with open('8/input.txt') as f:
    lines = f.read().splitlines()

instructions = lines[0].replace('L', '0').replace('R', '1')
nodes = []
# print(instructions)
way = defaultdict(tuple)
for line in lines[2:]:
    node, adjacent = line.split(' = (')
    left, right = adjacent.split(', ')
    way[node] = (left, right[0:-1])
    if node[-1] == 'A':
        nodes.append(node)

# print(way)
nbrOfSteps = []
nextStep = 0
newNodes = []
for node in nodes:
    nbr = 0
    startNode = node
    while(node[-1] != 'Z'):
        node = way[node][int(instructions[nextStep])]
        nextStep += 1 
        nextStep = nextStep % len(instructions)
        nbr += 1
    nbrOfSteps.append(nbr)

def findGCD(a, b):
    if a == b:
        return a
    if a > b:
        m = int(a/b) -1
        if m < 1:
            m = 1
        
        # print(a, b, m)
        return findGCD(a-b*m, b)
    else:
        m = int(b/a) -1
        if m < 1:
            m = 1
        # print(b, a, m)
        return findGCD(b-a*m, a)

def findLCM(a,b):
    # print(a,b)
    return (a/findGCD(a,b))*b

lcm = nbrOfSteps[0]
for steps in nbrOfSteps[1:]:
    lcm = findLCM(lcm, steps)

print(lcm)

# print(nbrOfSteps)

