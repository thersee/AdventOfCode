from queue import Queue
import sys

sys.setrecursionlimit(200000)
with open('23/input.txt') as f:
    lines = f.read().splitlines()

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adjacent = dict()

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

lastPos = (len(lines)-1, len(lines[0])-2)
nodes = dict()
def findAdjacent(pos, node, length, alreadyVisited):
    # print("#"*50)
    # print(pos)
    if lines[pos[0]][pos[1]] == '^':
        possibleSteps = [(-1,0)]
    elif lines[pos[0]][pos[1]] == 'v':
        possibleSteps = [(1,0)]
    elif lines[pos[0]][pos[1]] == '<':
        possibleSteps = [(0,-1)]
    elif lines[pos[0]][pos[1]] == '>':
        possibleSteps = [(0,1)]
    else :
        possibleSteps = [(-1,0), (1,0), (0,-1), (0,1)]
    possibilities = list()
    for a in possibleSteps:
        row = pos[0] + a[0]
        col = pos[1] + a[1]
        if row > -1 and row < len(lines[0]) and col > -1 and row < len(lines):
            if lines[row][col] != '#' and (row, col) not in alreadyVisited:
                possibilities.append((row,col))
    # print(possibilities)
    if len(possibilities) > 1:
        if pos in nodes:
            newNode = nodes[pos]
        else:
            newNode = Node(pos[0], pos[1])
            # print('appending',pos)
            nodes[pos] = newNode
        node.adjacent[pos] = length
        for p in possibilities:
            alreadyVisited.append(p)
            newvisited = alreadyVisited.copy()
            findAdjacent(p, newNode, 1, newvisited)
    elif len(possibilities) == 1:
        length += 1
        if possibilities[0] == lastPos:
            pos = possibilities[0]
            if pos in nodes:
                newNode = nodes[pos]
            else:
                newNode = Node(pos[0], pos[1])
                nodes[pos] = newNode
            node.adjacent[pos] = length
        else:
            alreadyVisited.append(possibilities[0])
            findAdjacent(possibilities[0], node, length, alreadyVisited)

startNode = Node(0,1)
nodes[(0,1)] = startNode
findAdjacent((0,1), startNode, 0, [(0,1)])

nextNodes = Queue()
nextNodes.put((startNode, 0))
maxWay = 0
while not nextNodes.empty():
    nextNode = nextNodes.get()
    node = nextNode[0]
    for adj, dist in node.adjacent.items():
        if adj == lastPos:
            way = nextNode[1] + dist
            if way > maxWay:
                maxWay = way
        else:
            nextNodes.put((nodes[adj], nextNode[1]+dist))



print(maxWay)

