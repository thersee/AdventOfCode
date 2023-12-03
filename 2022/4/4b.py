
with open('4/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 11258

sum = 0
for line in lines:
    vals = line.split(',')
    first = vals[0]
    f1, f2 = first.split('-')
    second = vals[1]
    s1, s2 = second.split('-')
    f1 = int(f1)
    f2 = int(f2)
    s1 = int(s1)
    s2 = int(s2)
    firstRange = [*range(f1, f2+1)]
    secondRange = [*range(s1, s2+1)]
    for i in firstRange:
        if i in secondRange:
            sum += 1
            break

print(sum)
