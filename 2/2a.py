
with open('2/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines]

def iWin(opp, me):
    if me == 'X' and opp == 'C':
        return True
    if me == 'Y' and opp == 'A':
        return True
    if me == 'Z' and opp == 'B':
        return True
    return False

def equal(opp, me):
    if me == 'X' and opp == 'A':
        return True
    if me == 'Y' and opp == 'B':
        return True
    if me == 'Z' and opp == 'C':
        return True
    return False

def val(me):
    if me == 'X':
        return 1
    if me == 'Y':
        return 2
    if me == 'Z':
        return 3

totalSum = 0
for line in lines:
    if iWin(line[0], line[2]):
        totalSum += 6+val(line[2])
    elif equal(line[0], line[2]):
        totalSum += 3+val(line[2])
    else:
        totalSum += val(line[2])
    

print(totalSum)