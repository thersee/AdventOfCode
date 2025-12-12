import sys
from queue import PriorityQueue
from functools import cmp_to_key
import re
import itertools

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

def pressButtons(buttonsToClick, target):
    result = [0]*len(target)
    for b in buttonsToClick:
        for ind in b:
            result[ind] += 1
    for i in range(len(result)):
        if result[i] % 2 == 0 and target[i] == '#':
            return False
        if result[i] % 2 == 1 and target[i] == '.':
            return False
    return True

totalPressed = 0
for line in lines:
    target = re.findall("\\[.*\\]", line)
    target = target[0][1:-1]
    #print(target)
    buttons = re.findall("(\\(.*\\))",line)
    buttons =buttons[0].split(' ')
    newButtons = list()
    for b in buttons:
        bns = b[1:-1].split(',')
        l = list()
        for bn in bns:
            l.append(int(bn))
        newButtons.append(l)
    buttons = newButtons
    #print(buttons)

    solved = False
    length = 1
    while not solved:
        toTry=set()
        allCombs = itertools.combinations(buttons, length)
        for c in allCombs:
            solved = pressButtons(c, target)
            if solved: 
                break
        length += 1
        
    totalPressed += length -1
print(totalPressed)
