from collections import defaultdict
from functools import cmp_to_key

with open('5/input.txt') as f:
    lines = f.read().splitlines()
    # lines = [int(x) for x in lines]

rules = defaultdict(list)
addRule = True
totalCorrect = 0

def sortPages(first, second):
    pagesAfterFirst = rules[first]
    pagesAfterSecond = rules[second]
    if second in pagesAfterFirst:
        return -1
    elif first in pagesAfterSecond:
        return 1
    else:
        return 0
    

for line in lines:
    if line == '':
        addRule = False
        continue
    if addRule:
        vals = line.split('|')
        rules[vals[0]].append(vals[1])
    else:
        lineOk = True
        pages = line.split(',')
        for index in range(0, len(pages)):
            page = pages[index]
            pageRules = rules[page]
            if len(set(pages[:index]).intersection(set(pageRules))):
                lineOk = False
                break
        if not lineOk:
            sortedList =sorted(pages, key=cmp_to_key(sortPages))
            totalCorrect += int(sortedList[int((len(sortedList)-1)/2)])
        


print(totalCorrect)