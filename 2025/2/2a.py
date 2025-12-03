import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

sumInvalid = 0
for line in lines:
    parts = line.split(',')
    for part in parts:
        interval = part.split('-')

        if interval == ['']:
            continue
        for i in range(int(interval[0]), int(interval[1])+1):
            s = str(i)
            l = len(s)
            if l %2 == 0:
                l = int(l/2)
            if s[0:l] == s[l:]:
                sumInvalid += int(s)

print(sumInvalid)