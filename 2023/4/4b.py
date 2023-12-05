from collections import defaultdict

with open('4/input.txt') as f:
    lines = f.read().splitlines()

numberOfCards = defaultdict(int)

totalPoints = 0
for index, line in enumerate(lines):
    numberOfCards[index] += 1
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
        # print(str(index) + ' has wins: '+ str(hits))
        for win in range(1, hits+1):
            numberOfCards[index+win] += numberOfCards[index]
        # print(numberOfCards)
        

print(sum(numberOfCards.values()))
    
    