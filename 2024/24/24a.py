import sys
from queue import Queue, PriorityQueue
from collections import defaultdict
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

class Node:
    def __init__(self, node1, node2, operator, value):
        self.node1 = node1
        self.node2 = node2
        self.operator = operator
        self.value = value
    
    def getOtherNode(self, n):
        if self.node1 == n:
            return self.node2
        elif self.node2 == n:
            return self.node1
    
    def calculate(self):
        n1 = allNodes[self.node1].value
        n2 = allNodes[self.node2].value
        # print(n1, n2)
        if n1 in [0,1] and n2 in [0,1]:
            # print('do it')
            if self.operator == 'AND':
                self.value = n1 & n2
                return self.value
            elif self.operator == 'XOR':
                self.value = n1 ^ n2
                return self.value
            else:
                self.value = n1 | n2
                return self.value
        
allNodes = dict()
calculations = defaultdict(list)
withValue = Queue()
outputTypes = True
zNodes = list()
for line in lines:
    if line == '':
        outputTypes = False
        continue
    if outputTypes:
        node = line.split(': ')
        if node[0][0] == 'z':
            zNodes.append(node[0])
        allNodes[node[0]] = Node(None, None, None, int(node[1]))
        withValue.put(node[0])
    else:
        l = line.split(' -> ')
        if l[1][0] == 'z':
            zNodes.append(l[1])
        ops = l[0].split(' ')
        allNodes[l[1]] = Node(ops[0], ops[2], ops[1], None)
        calculations[ops[0]].append(l[1])
        calculations[ops[2]].append(l[1])

while withValue.qsize():
    # print("#"*50)
    calc = withValue.get()
    # print(calc)
    possible = calculations[calc]
    calculated = set()
    for p in possible:
        # print(p)
        n = allNodes[p]
        if n.value == None:
            other = n.getOtherNode(calc)
            # print(other)
            if allNodes[other].value != None:
                # print('calculate', p)
                value = n.calculate()
                withValue.put(p)
                calculated.add(p)
        else: 
            calculated.add(p)
    possible = list(set(possible)-calculated)
    if len(possible) > 0:
        calculations[calc] = possible
        withValue.put(calc)

zNodes.sort(reverse=True)
value = ''
for n in zNodes:
    value += str(allNodes[n].value)

print(int(value,2))
