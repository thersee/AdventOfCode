import sys
import re
from scipy.optimize import linprog
import numpy as np

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()



totalPressed = 0
for line in lines:
    #print(line)
    target = re.findall("\\{.*\\}", line)
    target = target[0][1:-1].split(',')
    newTarget = list()
    for t in target:
        newTarget.append(int(t))
    target = newTarget
    buttons = re.findall("(\\(.*\\))",line)
    buttons =buttons[0].split(' ')
    newButtons = list()
    for b in buttons:
        bns = b[1:-1].split(',')
        l = list()
        for i in range(len(target)):
            if str(i) in bns:
                l.append(1)
            else:
                l.append(0)
        newButtons.append(l)
    buttons = newButtons
    #print(target)
    #print(buttons)
    A = np.array(buttons).transpose()
    b = np.array(target)
    c = np.ones(len(A[0]))
    #print(A)
    sol = linprog(c, A_eq=A, b_eq=b, integrality=1)
    totalPressed += sol.fun
print(totalPressed)