
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
            self.val = val
            return val

    def findVal(self, allNodes, value):
        
        if type(self.dep1) == str:
            missing = self.dep1
            if self.op == '+':
                newValue = value-self.dep2
            elif self.op == '-':
                newValue = value+self.dep2
            elif self.op == '*':
                newValue =int(value/self.dep2)
            elif self.op == '/':
                newValue = value*self.dep2
                
        else:
            missing = self.dep2
            if self.op == '+':
                newValue =  value-self.dep1
            if self.op == '-':
                newValue = self.dep1-value
            if self.op == '*':
                newValue = int(value/self.dep1)
            if self.op == '/':
                newValue = int(self.dep1/value)

        if missing == 'humn':
            print(newValue)
            return

        allNodes[missing].findVal(allNodes, newValue)


treeOps = defaultdict(list)
treeCalc = list()
allNodes = dict()

for line in lines:
    first = line.split(': ')
    name = first[0]
    operation = first[1].split(' ')
    val = None
    if not name == 'humn':
        if len(operation) == 1:
            treeCalc.append([name, int(operation[0])])
        else:
            node = TreeNode(name, None, operation[0], operation[2], operation[1])
            treeOps[operation[0]].append(node)
            treeOps[operation[2]].append(node)
            allNodes[name] = node

while treeCalc:
    n = treeCalc.pop(0)
    name = n[0]
    value = n[1]
    for node in treeOps[name]:
        val = node.setDep(name, value, treeCalc)

cand1 = allNodes['rpjn']
cand2 = allNodes['ghjl']

if cand1.val == None:
    cand1.findVal(allNodes, cand2.val)
else:
    cand2.findVal(allNodes, cand1.val)




    
