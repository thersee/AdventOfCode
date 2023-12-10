from functools import cmp_to_key
from collections import defaultdict
with open('7/input.txt') as f:
    lines = f.read().splitlines()
values = 'AKQT98765432J'

def getrank(hand):
    # print("#"*50)
    # print(hand)
    found = defaultdict(int)
    jokers = 0
    for val in values:
        double = hand.count(val)
        if val == 'J':
            # print(double)
            jokers = double
        else:
            # print(val, double)
            found[val] = double
    doubles = list(found.values())
    # print(doubles)
    if doubles.count(5) == 1:
        return 7
    elif doubles.count(4) == 1:
        if jokers == 1:
            return 7
        return 6
    elif doubles.count(3) == 1 and doubles.count(2) == 1:
        return 5
    elif doubles.count(3) == 1:
        if jokers == 1:
            # print('should be here')
            return 6
        elif jokers == 2:
            return 7
        return 4
    elif doubles.count(2) == 2:
        if jokers == 1:
            return 5
        # print('next here')
        return 3
    elif doubles.count(2) == 1:
        # print(jokers)
        if jokers == 1:
            return 4
        elif jokers == 2:
            return 6
        elif jokers == 3:
            return 7
        # print('and here')
        return 2
    elif doubles.count(1) == 5:
        return 1
    elif jokers == 5:
        return 7
    elif jokers == 4:
        return 7
    elif jokers == 3:
        return 6
    elif jokers == 2:
        return 4
    elif jokers == 1:
        return 2

def sortCards(a, b):
    handA = a.split(' ')[0]
    handB = b.split(' ')[0]
    # print("#"*50)
    rankA = getrank(handA)
    rankB = getrank(handB)
    # print(handA, handB)
    # print(rankA, rankB)
    if rankA > rankB:
        return -1
    elif rankB > rankA:
        return 1
    else:
        for i in range(0, len(handA)):
            if values.find(handA[i]) > values.find(handB[i]):
                # print('a before b')
                return 1
            elif values.find(handA[i]) < values.find(handB[i]):
                # print('b before a')
                return -1
    
    

# print(getrank(lines[0].split(' ')[0]))
lines = sorted(lines, key=cmp_to_key(sortCards))
# print(lines)
totalScore = 0

for index, line in enumerate(lines):
    # print((len(lines) - index), int(line.split(' ')[1]))
    totalScore += (len(lines) - index)*int(line.split(' ')[1])

print(totalScore)