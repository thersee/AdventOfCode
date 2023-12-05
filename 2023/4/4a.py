with open('4/input.txt') as f:
    lines = f.read().splitlines()

totalPoints = 0
for line in lines:
    # print("#"*50)
    numbers = line.split(':')[1]
    splitted = numbers.split('|')
    winning = splitted[0].strip()
    yourNumbers = splitted[1].strip()
    winningList = winning.split(' ')
    yourList = yourNumbers.split(' ')

    # print(yourList)
    # print(winningList)


    hits = 0
    for y in yourList:
        if y.isdigit() and y in winningList:
            hits += 1
    if hits > 0:
        # print(hits)
        totalPoints += 2**(hits-1)

print(totalPoints)
    
    