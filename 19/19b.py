import copy
#183 too low
with open('19/input.txt') as f:
    lines = f.read().splitlines()

class Blueprint():
    def __init__(self, oreCost, clayCost, obsCost, geodeCost):
        self.oreCost = oreCost
        self.clayCost = clayCost
        self.obsCost = obsCost
        self.geodeCost = geodeCost
        self.maxOre = max(oreCost[0], clayCost[0], obsCost[0][0],geodeCost[0][0])

blueprints = dict()
i = 0
while i < 3:
    line = lines[i]
    first = line.split(':')
    blueprintId = int(first[0].split(' ')[-1])
    second = first[1].split('. ')

    ore = second[0].split(' ')
    oreCost = (int(ore[5]), 'ore')
    clay = second[1].split(' ')
    clayCost = (int(clay[4]), 'ore')
    obs = second[2].split(' ')
    obsCost = [(int(obs[4]), 'ore'), (int(obs[7]), 'clay')]
    geode = second[3].split(' ')
    geodeCost = [(int(geode[4]), 'ore'), (int(geode[7]), 'obs')]
    blueprints[blueprintId] = Blueprint(oreCost, clayCost, obsCost, geodeCost)
    i += 1

allRobots = ['ore', 'clay', 'obs', 'geode']

def timeToProduce(cost, resource, robots, availableResources):
    time = 0
    material = availableResources[resource]
    while material < cost:
        for robot in robots:
            if robot == resource:
               material += 1
        time += 1
    return time

def produce(time, robots, availableResources):
    for i in range(0,time):
        for robot in robots:
            availableResources[robot] += 1

quality =1
for id, blueprint in blueprints.items():

    maxGeode = 0
    nextTurn = [['ore', 32, ['ore'], {'ore': 0, 'clay': 0, 'obs': 0, 'geode': 0}]]
    while nextTurn:
        node = nextTurn.pop(0)
        availableRobots = node[2]
        # print(len(nextTurn), node[1])

        # print("#"*50)
        # print(availableRobots.count('ore'))
        # print(availableRobots.count('clay'))
        # print(availableRobots.count('obs'))
        # print(availableRobots.count('geode'))
        timeLeft = node[1]
        availableResources = node[3]
        theoreticalMax = availableRobots.count('geode')*timeLeft+availableResources['geode']+timeLeft*(timeLeft-1)/2
        if theoreticalMax <= maxGeode:
            continue
        if availableResources['geode'] > maxGeode:
            maxGeode = availableResources['geode']

        if 'clay' in availableRobots and availableRobots.count('obs') < blueprint.geodeCost[1][0]:
            availableRobotsObs = copy.deepcopy(availableRobots)
            availableResourcesObs = copy.deepcopy(availableResources)
            costInOre = blueprint.obsCost[0][0]
            timeToOre = 0
            timeToClay = 0
            if availableResourcesObs['ore'] < costInOre:
                timeToOre = timeToProduce(costInOre, 'ore', availableRobotsObs, availableResourcesObs)
            costInClay = blueprint.obsCost[1][0]
            if availableResourcesObs['clay'] < costInClay:
                timeToClay = timeToProduce(costInClay, 'clay', availableRobotsObs, availableResourcesObs)
            totalTime = max(timeToClay, timeToOre)+1
            if timeLeft-totalTime>= 0:
                produce(totalTime, availableRobotsObs, availableResourcesObs)
                availableRobotsObs.append('obs')
                availableResourcesObs['ore'] -= costInOre
                availableResourcesObs['clay'] -= costInClay
                nextTurn.append(['obs', timeLeft-totalTime, availableRobotsObs, availableResourcesObs])

        if 'obs' in availableRobots:
            availableRobotsGeode = copy.deepcopy(availableRobots)
            availableResourcesGeode = copy.deepcopy(availableResources)
            costInOre = blueprint.geodeCost[0][0]
            timeToOre = 0
            timeToObs = 0
            if availableResourcesGeode['ore'] < costInOre:
                timeToOre = timeToProduce(costInOre, 'ore', availableRobotsGeode, availableResourcesGeode)
            costInObs = blueprint.geodeCost[1][0]
            if availableResourcesGeode['obs'] < costInObs:
                timeToObs = timeToProduce(costInObs, 'obs', availableRobotsGeode, availableResourcesGeode)
            totalTime = max(timeToObs, timeToOre)+1
            if timeLeft-totalTime>= 0:
                produce(totalTime, availableRobotsGeode, availableResourcesGeode)
                availableRobotsGeode.append('geode')
                availableResourcesGeode['ore'] -= costInOre
                availableResourcesGeode['obs'] -= costInObs
                nextTurn.append(['geode', timeLeft-totalTime, availableRobotsGeode, availableResourcesGeode])
                
        if availableRobots.count('ore') < blueprint.maxOre:
            availableRobotsOre = copy.deepcopy(availableRobots)
            availableResourcesOre = copy.deepcopy(availableResources)
            cost = blueprint.oreCost[0]
            time = 0
            if availableResourcesOre['ore'] < cost:
                time = timeToProduce(cost, 'ore', availableRobotsOre, availableResourcesOre)
            totalTime = time+1
            if timeLeft-totalTime >= 0:
                produce(totalTime, availableRobotsOre, availableResourcesOre)
                availableRobotsOre.append('ore')
                availableResourcesOre['ore'] -= cost
                nextTurn.append(['ore', timeLeft-totalTime, availableRobotsOre, availableResourcesOre])


        if availableRobots.count('clay') < blueprint.obsCost[1][0]:
            availableRobotsClay = copy.deepcopy(availableRobots)
            availableResourcesClay = copy.deepcopy(availableResources)
            cost = blueprint.clayCost[0]
            time = 0
            if availableResourcesClay['ore'] < cost:
                time = timeToProduce(cost, 'ore', availableRobotsClay, availableResourcesClay)
            totalTime = time +1
            if timeLeft-totalTime >= 0:
                produce(totalTime, availableRobotsClay, availableResourcesClay)
                availableRobotsClay.append('clay')
                availableResourcesClay['ore'] -= cost
                nextTurn.append(['clay', timeLeft-totalTime, availableRobotsClay, availableResourcesClay])

    quality*=maxGeode

print(quality)
    