with open('11/input.txt') as f:
    lines = f.read().splitlines()

def blink(stone):
    if int(stone) == 0:
        return ['1']
    
    if len(stone)%2 == 0:
        return [str(int(stone[:int(len(stone)/2)])), str(int(stone[int(len(stone)/2):]))]
    return [str(int(stone)*2024)]

stones = lines[0].split(' ')
for i in range(25):
    newStones = []
    for stone in stones:
        newStones.extend(blink(stone))
    stones = newStones

print(len(stones))