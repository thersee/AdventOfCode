import copy
with open('16/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 


class Valve:
    def __init__(self, name, flowRate, tunnels):
        self.name = name
        self.flowRate = flowRate
        self.tunnels = tunnels
        self.distances = dict()

valves = dict()
valvesOpened = dict()

for line in lines:
    words = line.split(' ')
    name = words[1]
    flowRate = int(words[4][5:-1])
    i = -1
    tunnels = words[i]
    tList = list()
    while tunnels not in ['valve', 'valv']:
        tList.append(tunnels)
        i -= 1
        tunnels = words[i][:-1]

    valves[name] = Valve(name, flowRate, tList)

numberOfNonZero = 0
for name, valve in valves.items():
    if valve.flowRate > 0:
        numberOfNonZero += 1
    distances = dict()
    toExplore = [[name, -1]]
    while toExplore:
        node = toExplore.pop(0)
        if node[0] not in distances or distances[node[0]] > node[1] +1:
            distances[node[0]] = node[1] +1
            for tunnel in valves[node[0]].tunnels:
                toExplore.append([tunnel, node[1] +1])
    valve.distances = distances

toExplore = list()
toExplore.append(['AA', 26, 0, list()])
maxLostPressure = 0
opened = dict()


while len(toExplore) > 0:
    nextValve = toExplore.pop(0)
    valveName = nextValve[0]
    timeLeft = nextValve[1]
    pressureLost = nextValve[2]
    openedValves = nextValve[3]

    openedValves.sort()
    k = str(openedValves)
    if k not in opened or opened[k] < pressureLost:
        opened[k] = pressureLost

    if pressureLost > maxLostPressure:
        maxLostPressure = pressureLost

    if len(openedValves) < numberOfNonZero and timeLeft > 0:
        for tunnel, dist in valves[valveName].distances.items():
            if tunnel not in openedValves and valves[tunnel].flowRate > 0 and dist < timeLeft +1:
                newtimeLeft = timeLeft - dist -1
                newPressureLost = pressureLost + newtimeLeft * valves[tunnel].flowRate
                openedValves1 = copy.deepcopy(openedValves)
                openedValves1.append(tunnel)
                toExplore.append([tunnel, newtimeLeft, newPressureLost, openedValves1])

twoMaxPressure = 0
for list, pressure in opened.items():
    for list2, pressure2 in opened.items():
        if not set(eval(list)) & set(eval(list2)):
            if pressure + pressure2 > twoMaxPressure:
                twoMaxPressure = pressure2 + pressure

print(twoMaxPressure)