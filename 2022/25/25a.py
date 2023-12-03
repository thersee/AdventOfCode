with open('25/input.txt') as f:
    lines = f.read().splitlines()

converter = {'=': -2, '-':-1, '0':0, '1':1, '2': 2}

sum = 0
for line in lines:
    number = 0
    base = 1
    for char in range(len(line)-1, -1, -1):
        number += converter[line[char]]*base
        base *= 5
    sum += number
print(sum)

output = ''

while sum:
    rem = sum%5
    if rem == 3:
        output = '=' + output
        sum = int(sum/5+1)
    
    elif rem == 4:
        output = '-' + output
        sum = int(sum/5+1)
    else:
        output = str(rem) + output
        sum = int(sum/5)
    
print(output)



