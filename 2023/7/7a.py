from functools import cmp_to_key
from collections import defaultdict
with open('7/input.txt') as f:
    lines = f.read().splitlines()
values = 'AKQJT98765432'

def getrank(hand):
    found = defaultdict(int)
    for val in values:
        double = hand.count(val)
        # print(val, double)
        found[val] = double
    doubles = list(found.values())
    # print(doubles)
    if doubles.count(5) == 1:
        return 700000
    elif doubles.count(4) == 1:
        return 600000
    elif doubles.count(3) ==1 and doubles.count(2) == 1:
        return 500000
    elif doubles.count(3) == 1:
        return 400000
    elif doubles.count(2) == 2:
        return 300000
    elif doubles.count(2) == 1:
        return 200000
    elif doubles.count(1) == 5:
        return 100000

def sortCards(a, b):
    handA = a.split(' ')[0]
    handB = b.split(' ')[0]
    rankA = getrank(handA)
    rankB = getrank(handB)
    # print(rankA, rankB)
    if rankA > rankB:
        return -1
    elif rankB > rankA:
        return 1
    else:
        for i in range(0, len(handA)):
            if values.find(handA[i]) > values.find(handB[i]):
                return 1
            elif values.find(handA[i]) < values.find(handB[i]):
                return -1
    
    

# print(getrank(lines[0].split(' ')[0]))
lines = sorted(lines, key=cmp_to_key(sortCards))
# print(lines)
totalScore = 0

for index, line in enumerate(lines):
    # print((len(lines) - index), int(line.split(' ')[1]))
    totalScore += (len(lines) - index)*int(line.split(' ')[1])

print(totalScore)