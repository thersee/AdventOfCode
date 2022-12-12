from collections import defaultdict

with open('11/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 


divider = 1
class Monkey:
    def __init__(self, number, op, nbr, test, tr, fa, items):
        self.number = number
        self.op = op
        self.nbr = nbr
        self.test = test
        self.ifTrue = tr
        self.ifFalse = fa
        self.items = items
        self.seenItems = 0

    def getItems(self):
        items = self.items
        self.items = list()
        self.seenItems += len(items)
        return items

    def perform(self, item):
        global divider
        if self.nbr == 'old':
            nbr = int(item)
        else:
            nbr = int(self.nbr)
        if self.op == '+':
            val =item+nbr
        elif self.op == '*':
            val = item*nbr
        val = int(val % divider)
        if val % self.test == 0:
            return self.ifTrue, val
        else:
            return self.ifFalse, val


monkeys = list()

monkey = 0
index = 0
while monkey < len(lines)/7:
    index += 1
    items = lines[index].split(': ')[1].split(', ')
    items = [int(x) for x in items] 
    index += 1
    op = lines[index].split(' ')[-2]
    nbr = lines[index].split(' ')[-1]
    index += 1
    test = int(lines[index].split(' ')[-1])
    divider *= test
    index += 1
    tr = int(lines[index].split(' ')[-1])
    index += 1
    fa = int(lines[index].split(' ')[-1])
    index += 1
    index += 1

    monkeys.append(Monkey(monkey, op, nbr, test, tr, fa, items))
    monkey += 1

rounds = 10000
for i in range(0, rounds):
    for j in range(0, len(monkeys)):
        monkey = monkeys[j]
        items = monkey.getItems()
        for item in items:
            sendTo, newItem = monkey.perform(item)
            monkeys[sendTo].items.append(newItem)

seen = list()
for monkey in monkeys:
    seen.append(monkey.seenItems)

seen.sort()
print(seen[-1]*seen[-2])