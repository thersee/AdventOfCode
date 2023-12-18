with open('15/input.txt') as f:
    lines = f.read().splitlines()

line = lines[0]
values = line.split(',')

totalSum = 0
for value in values:
    thisSum = 0
    for c in range(0, len(value)):
        thisSum += ord(value[c])
        thisSum *= 17
        thisSum = thisSum % 256
    # print(thisSum)
    totalSum += thisSum

print(totalSum)
