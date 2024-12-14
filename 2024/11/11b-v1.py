from collections import defaultdict
from functools import cache

with open('11/input.txt') as f:
    lines = f.read().splitlines()

myCache = defaultdict(list)

@cache
def blink(stone):
    if int(stone) == 0:
        return ['1']
    
    elif len(stone)%2 == 0:
        return [str(int(stone[:int(len(stone)/2)])), str(int(stone[int(len(stone)/2):]))]
    else:
        return [str(int(stone)*2024)]
    
@cache
def iterate(stone, iterations):
    stones = blink(stone)
    if iterations <= 1:
        return stones
    
    stonesToReturn = []
    for s in stones:
        stonesToReturn.extend(iterate(s, iterations -1))
    
    return stonesToReturn
    
stones = lines[0].split(' ')
newStones = []
for stone in stones:
    newStones.extend(iterate(stone, 75))
stones = newStones

print(len(stones))