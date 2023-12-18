from queue import PriorityQueue
import sys

with open('17/input.txt') as f:
    lines = f.read().splitlines()

class Node():
    def __init__(self, xInit, yInit, heatlossInit, dirInit):
        self.heatLoss = heatlossInit
        self.totalheatLoss = sys.maxsize
        self.x = xInit
        self.y = yInit
        self.dir = dirInit
        self.visited = False

    def __str__(self):
        return 'totalheatLoss: ' + str(self.totalheatLoss) + ' (' + \
        str(self.x) + ', ' + str(self.y) + ') dir: '+ self.dir +' visited: ' + str(self.visited)

    def __lt__(self, other):
        return self.totalheatLoss < other.totalheatLoss


def evalNeighbours(neighbours):
    for n in neighbours:
        nextNode = allNodes[n]
        # print(nextNode)
        if not nextNode.visited:
            newHeatloss = current.totalheatLoss - current.heatLoss
            for i in range(min(current.x, nextNode.x), max(current.x, nextNode.x)+1):
                for j in range(min(current.y, nextNode.y), max(current.y, nextNode.y)+1): 
                    # print(i,j)    
                    # print(allNodes[(i,j,'v')].heatLoss) 
                    newHeatloss += allNodes[(i,j,'v')].heatLoss
            # print(newHeatloss)
            if newHeatloss < nextNode.totalheatLoss:
                nextNode.totalheatLoss = newHeatloss
            # print('put node with ' + str(nextNode.totalheatLoss))
            q.put(nextNode)

def getNeigbours(row, col, dir):
    neighbours = list()
    if dir == 'h':
        for i in [-10,-9,-8,-7,-6,-5,-4,4,5,6,7,8,9,10]:
            if row + i >= 0 and row +i < len(lines):
                neighbours.append((row+i, col, 'v'))
    elif dir == 'v':
        for i in [-10,-9,-8,-7,-6,-5,-4,4,5,6,7,8,9,10]:
            if col + i >= 0 and col +i < len(lines[0]):
                neighbours.append((row, col+i, 'h'))
    return neighbours

allNodes = dict()
q = PriorityQueue()

current = Node(0,0,int(lines[0][0]),'x')
current.totalheatLoss = 0
for row, line in enumerate(lines):
    for col in range(0, len(line)):
        n = Node(row, col, int(line[col]), 'h')
        allNodes[(row, col, 'h')] = n
        n = Node(row, col, int(line[col]), 'v')
        allNodes[(row, col, 'v')] = n

firstNeighbours = [(0,4,'h'), (0,5,'h'),(0,6,'h'),(0,7,'h'), (0,8,'h'),(0,9,'h'),(0,10,'h'),(4,0,'v'), (5,0,'v'),(6,0,'v'),(7,0,'v'),(8,0,'v'),(9,0,'v'),(10,0,'v')]
evalNeighbours(firstNeighbours)

# current = q.get()
run = True
while run:
    current = q.get()
    # print(current)
    if not current.visited:
        # print(current)
        neighbours = getNeigbours(current.x, current.y, current.dir)
        # print(neighbours)
        evalNeighbours(neighbours)
        current.visited = True
        if current.x == len(lines)-1 and current.y == len(lines[0])-1:
            run = False

print(current)
    