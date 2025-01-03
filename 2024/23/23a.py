import sys
from queue import Queue, PriorityQueue
from collections import defaultdict
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

connections = defaultdict(list)
for line in lines:
    comp1, comp2 = line.split('-')
    connections[comp1].append(comp2)
    connections[comp2].append(comp1)

triangles = set()
for key in connections.keys():
    if key[0] == 't':
        for node1 in connections[key]:
            for node2 in connections[key]:
                if node2 in connections[node1]:
                    triangle = [key, node1, node2]
                    triangle.sort()
                    triangles.add(tuple(triangle))

print(len(triangles))