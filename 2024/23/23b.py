import sys
from queue import Queue, PriorityQueue
from collections import defaultdict
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

connections = defaultdict(set)
for line in lines:
    comp1, comp2 = line.split('-')
    connections[comp1].add(comp2)
    connections[comp2].add(comp1)

def isConnected(nodes):
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j and nodes[j] not in connections[nodes[i]]:
                return False
    return True

#Hint from reddit: input seem to be nice so one node part of a small clique 
#will not be parts of the greater, better. Thus, nodes found in a clique can
#be disregarded when seaching for another for that node. Searching for best clique
#for all starting nodes like this will give the answer
answer = ''
for key in connections.keys():
    nodes = list()
    nodes.append(key)
    neigbours = list(connections[key])
    while len(neigbours) > 0:
        for i in range(len(neigbours)):
            nodes.append(neigbours[i])
            if not isConnected(nodes):
                nodes.remove(neigbours[i])
        nodes.sort()
        thisAnswer = ','.join(nodes)
        if len(thisAnswer) > len(answer):
            answer = thisAnswer
        nodes.remove(key)
        neigbours = list(set(neigbours)-set(nodes))
        nodes = list()
        nodes.append(key)

print(answer)
        