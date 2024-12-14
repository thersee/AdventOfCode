from collections import defaultdict

with open('5/input.txt') as f:
    lines = f.read().splitlines()
    # lines = [int(x) for x in lines]

rules = defaultdict(list)
addRule = True
totalCorrect = 0

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
        if lineOk:
            print((len(pages)-1)/2, pages)
            totalCorrect += int(pages[int((len(pages)-1)/2)])
        


print(totalCorrect)