import functools

with open('13/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 


def comp(left, right):
    if type(left) == int and type(right) == 0:
        return left-right
    if len(left) == 0 and len(right) == 0:
        return 0
    elif len(left) == 0:
        return -1
    elif len(right) == 0:
        return 1
    val = 0
    if type(left[0])== list and type(right[0]) == list:
        val=comp(left[0], right[0])
    elif type(left[0])== int and type(right[0]) == list:
        val=comp([left[0]], right[0])
    elif type(left[0])== list and type(right[0]) == int:
        val=comp(left[0], [right[0]])
    elif type(left[0])== int and type(right[0]) == int:
        val = left[0] - right[0]
    if val == 0:
        val = comp(left[1:], right[1:])
    return val

allLines = list()
allLines.append([[2]])
allLines.append([[6]])
for line in lines:
    if line != '':
        allLines.append(eval(line))

allLines = sorted(allLines, key=functools.cmp_to_key(comp))

m = 1
index = 1
for line in allLines:
    if line == [[2]] or line == [[6]]:
        m *= index
    index += 1

print(m)