
with open('1/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines]


integers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1','2', '3', '4', '5','6','7','8','9']

def con(a, b):
    if not a.isdigit():
        a = str(integers.index(a) + 1)
    if not b.isdigit():
        b = str(integers.index(b) + 1)
    print(a+b)
    return a+b

sum = 0
for i in range(0, len(lines)):
    line = lines[i]
    smallestIndex = len(line)
    largestIndex = -1
    firstNumber = -1
    lastNumber = -1
    for i in integers:
        firstIndex = line.find(i)
        lastIndex = line.rfind(i)
        if firstIndex > -1 and firstIndex < smallestIndex:
            smallestIndex = firstIndex
            firstNumber = i
        if lastIndex > -1 and lastIndex > largestIndex:
            largestIndex = lastIndex
            lastNumber = i
    sum = sum + int(con(firstNumber, lastNumber))
    
    

print(sum)
