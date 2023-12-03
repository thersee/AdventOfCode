
with open('2/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 11258

#if win:
def chooseLoose(opp):
    if opp == 'A':
        return 'C'
    elif opp == 'B':
        return 'A'
    else:
        return 'B'

#if loose
def chooseWin(opp):
    if opp == 'A':
        return 'B'
    elif opp == 'B':
        return 'C'
    else:
        return 'A'


def val(me):
    if me == 'A':
        return 1
    if me == 'B':
        return 2
    if me == 'C':
        return 3

totalSum = 0
for line in lines:
    outcome = line[2]
    if outcome == 'Z':
        totalSum += 6+val(chooseWin(line[0]))
    elif outcome == 'Y':
        totalSum += 3+val(line[0])
    else:
        totalSum += val(chooseLoose(line[0]))
    

print(totalSum)