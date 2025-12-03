import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

cur = 50
timesZero = 0
for line in lines:
    d = line[0]
    num = int(line[1:])
    if d == 'L':
        cur -= num 
    else:
        cur += num
    cur = (cur+100) % 100

    if cur == 0:
        timesZero += 1

print(timesZero)