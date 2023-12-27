import networkx as nx

with open('25/input.txt') as f:
    lines = f.read().splitlines()

class Node():
    def __init__(self, name, attached):
        self.name = name
        self.attached = attached

nodes = dict()
for line in lines:
    n = line.split(': ')
    node = n[0]
    nextToNodes = n[1].split(' ')
    if node in nodes:
        ny = nodes[node]
        ny.attached.extend(nextToNodes)
    else:
        ny = Node(node, nextToNodes)
        nodes[node] = ny
    for otherNode in nextToNodes:
        if otherNode in nodes:
            my = nodes[otherNode]
            my.attached.append(node)
        else:
            my = Node(otherNode, [node])
            nodes[otherNode] = my

g = nx.Graph()
for name, node in nodes.items():
    for att in node.attached:
        g.add_edge(name, att)   

r = nx.community.louvain_communities(g,resolution=0.003,  seed=79)
print(len(r[0])* len(r[1]))



