with open('7/input.txt') as f:
    lines = f.read().splitlines()
    # lines = [int(x) for x in lines]

def doIt(operand, numbers, thisSum, totalSum):
    if thisSum > totalSum:
        return False
    if not numbers or len(numbers) == 0:
        if thisSum == totalSum:
            return True
        else:
            return False
        
    num = int(numbers[0])
    if operand == 'p':
        thisSum += num
        plus = doIt('p', numbers[1:], thisSum, totalSum)
        mul = doIt('m', numbers[1:], thisSum, totalSum)
        con = doIt('c', numbers[1:], thisSum, totalSum)
    elif operand == 'm':
        thisSum *= num
        plus = doIt('p', numbers[1:], thisSum, totalSum)
        mul = doIt('m', numbers[1:], thisSum, totalSum)
        con = doIt('c', numbers[1:], thisSum, totalSum)
    elif operand == 'c':
        if thisSum == -1:
            thisSum = ''
        newNumber = int(str(thisSum)+numbers[0])

        plus = doIt('p', numbers[1:], newNumber, totalSum)
        mul = doIt('m', numbers[1:], newNumber, totalSum) 
        con = doIt('c', numbers[1:], newNumber, totalSum)

    if plus or mul or con:
        return True
    else:
        return False

allOk = 0
for line in lines:
    first = line.split(':')
    totalSum = int(first[0])
    numbers = first[1].strip().split(' ')
    plus = doIt('p', numbers, 0, totalSum)
    mul = doIt('m', numbers, 1, totalSum)
    con = doIt('c', numbers, -1, totalSum)
    if plus or mul or con:
        # print(line)
        allOk += totalSum


print(allOk)
