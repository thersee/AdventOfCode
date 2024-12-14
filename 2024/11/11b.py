from collections import defaultdict
with open('11/input.txt') as f:
    lines = f.read().splitlines()

def blink(stone):
    if int(stone) == 0:
        return ['1']
    
    if len(stone)%2 == 0:
        return [str(int(stone[:int(len(stone)/2)])), str(int(stone[int(len(stone)/2):]))]
    return [str(int(stone)*2024)]

stones = defaultdict(int)
for s in lines[0].split(' '):
    stones[s] += 1

for i in range(75):
    newStones = defaultdict(int)
    for stone in stones.keys():
        rStones = blink(stone)
        for s in rStones:
            newStones[s] += 1*stones[stone]
    stones = newStones

nbrOfStones = 0
for v, nbr in stones.items():
    nbrOfStones += nbr
print(nbrOfStones)