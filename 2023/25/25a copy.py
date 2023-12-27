with open('25/inputTest.txt') as f:
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



