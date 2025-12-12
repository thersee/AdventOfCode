import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

graph = dict()
for line in lines:
    key, nodes = line.split(': ')
    connected = nodes.split(' ')
    graph[key] = connected

print(graph)

def dfs(curr, dest, graph, count):
    if curr == dest:
        count[0] += 1
        return
    
    for n in graph[curr]:
        dfs(n, dest, graph, count)
        
tot = [0]
dfs("you", "out", graph, tot)
print(tot)

    