import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

fresh = list()

empty = False
i = 0
while not empty:
    line = lines[i]
    if line == "":
        break
    ints = line.split('-')
    fresh.append((int(ints[0]), int(ints[1])))
    i += 1

numFresh = 0
for i in range(i+1,len(lines)):
    line = int(lines[i])
    for pair in fresh:
        if line >= pair[0] and line <= pair[1]:
            print(line, pair)
            numFresh += 1
            break
print(numFresh)
