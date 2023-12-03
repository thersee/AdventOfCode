from collections import defaultdict

with open('10/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 

x = 1
round = 0
signal = 0

def addSignal():
    global round
    global x
    global signal
    round += 1

    if round in [20, 60, 100, 140, 180, 220]:
        signal += round*x

for line in lines:
    c = line.split(' ')
    if c[0] == 'noop':
        addSignal()
    else:
        addSignal()
        addSignal()
        x += int(c[1])


print(signal)