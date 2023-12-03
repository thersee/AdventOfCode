from collections import defaultdict

with open('6/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 11258
line = lines[0]
i = 0
prev = list()

while i < len(line):
    if len(prev) == 13 and line[i] not in prev:
        i += 1
        break
    while line[i] in prev:
        prev.pop(0)
    prev.append(line[i])
    i += 1
    
print(i)