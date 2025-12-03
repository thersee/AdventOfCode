import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

tot = 0
for line in lines:
    max = '0'
    sec = '0'
    for i in range(len(line)):
        if i != len(line)-1 and line[i] > max:
            max = line[i]
            sec = line[i+1]
        elif line[i] > sec:
            sec = line[i]
    tot += int(max+sec)

print(tot)