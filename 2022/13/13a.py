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

okRows = list()
indices = 0
for i in range(0,len(lines), 3):
    indices += 1
    left=eval(lines[i])
    right=eval(lines[i+1])
    v= comp(left, right)
    if comp(left, right) < 0:
        okRows.append(indices)
print(sum(okRows))