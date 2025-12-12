import sys
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()


global graph 
graph= dict()
for line in lines:
    key, nodes = line.split(': ')
    connected = nodes.split(' ')
    graph[key] = connected

@cache
def dfs(curr, dest, count):
    if curr == dest:
        count += 1
        return count
    
    if curr == "out":
        return count
    newCount = 0
    for n in graph[curr]:
        newCount += dfs(n, dest, 0)
    count += newCount
    return count

all1 = 1
c = dfs("svr", "dac", 0)
all1 *= c

c =dfs("dac", "fft", 0)
all1 *= c


c =dfs("fft", "out", 0)
all1 *= c

all2 = 1
c = dfs("svr", "fft", 0)
all2 *= c

c =dfs("fft", "dac", 0)
all2 *= c


c =dfs("dac", "out", 0)
all2 *= c
print(all1)
print(all2)
print(all1+all2)

    