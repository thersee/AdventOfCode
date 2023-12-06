import re

with open('6/input.txt') as f:
    lines = f.read().splitlines()

time = ''.join(re.findall(r'\d+', lines[0].split(':')[1]))
oldRecord = ''.join(re.findall(r'\d+', lines[1].split(':')[1]))

time = int(time)

better = 0
for t in range(1,time):
    dist = t * (time-t)
    if dist > int(oldRecord):
        better += 1


print(better)


