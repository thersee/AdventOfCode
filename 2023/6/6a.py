import re

with open('6/input.txt') as f:
    lines = f.read().splitlines()

times = re.findall(r'\d+', lines[0].split(':')[1])
oldRecord = re.findall(r'\d+', lines[1].split(':')[1])

totalMargin = 1
for race, time in enumerate(times):
    time = int(time)
    better = 0
    for t in range(1,time):
        dist = t * (time-t)
        if dist > int(oldRecord[race]):
            better += 1
    if better > 0:
        totalMargin *= better

print(totalMargin)


