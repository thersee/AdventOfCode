from collections import defaultdict

with open('10/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 

x = 1
round = 0
signal = 0

crt=''

def addSignal():
    global round
    global x
    global signal
    global crt
    round += 1

    print(x)
    if x-1 <= len(crt)%40 <= x+1:
        crt += '#'
    else:
        crt += ' '
    
    
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


print(crt[0:40])
print(crt[40:80])
print(crt[80:120])
print(crt[120:160])
print(crt[160:200])
print(crt[200:240])