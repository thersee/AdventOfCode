
from collections import defaultdict
with open('21/input.txt') as f:
    lines = f.read().splitlines()

class TreeNode:
    def __init__(self, name, val, dep1, dep2, op):
        self.name = name
        self.val = val
        self.dep1 = dep1
        self.dep2 = dep2
        self.op = op

    def setDep(self, dep, val, treeCalc):
        if dep == self.dep1:
            self.dep1 = val
        else:
            self.dep2 = val
        
        if type(self.dep1) == int and type(self.dep2) == int:
            val = eval(str(self.dep1)+ '' +self.op+''+str(self.dep2))
            treeCalc.append([self.name, int(val)])
            return val


treeOps = defaultdict(list)
treeCalc = list()

for line in lines:
    first = line.split(': ')
    name = first[0]
    operation = first[1].split(' ')
    val = None
    if len(operation) == 1:
        treeCalc.append([name, int(operation[0])])
    else:
        node = TreeNode(name, None, operation[0], operation[2], operation[1])
        treeOps[operation[0]].append(node)
        treeOps[operation[2]].append(node)

while treeCalc:
    n = treeCalc.pop(0)
    name = n[0]
    value = n[1]

    for node in treeOps[name]:
        val = node.setDep(name, value, treeCalc)
        if node.name == 'root':
            print(val)
    
