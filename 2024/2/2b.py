with open('2/input.txt') as f:
    lines = f.read().splitlines()
    # lines = [int(x) for x in lines]

def isLineOk(l):
    inc = l[1] - l[0] > 0
    for j in range(0, len(l)-1):
        if l[j+1] - l[j] > 0 and inc:
            if l[j+1] - l[j] > 3:
                return j+1
        elif l[j+1] - l[j] < 0 and not inc:
            if l[j+1] - l[j] < -3:
                return j+1
        else:
            return j+1
            
    return -1

sum = 0
oldSUm = 0
for i in range(0, len(lines)):
    line = lines[i].split(' ')
    line = [int(x) for x in line]
    inc = line[1] - line[0] > 0
    ok = True
    removed = False
    ind = isLineOk(line)

    if ind > 0:
        anyOk = []
        # print("#"*20)
        for k in range(0,len(line)):
            anyOk = isLineOk(line[:k]+line[k+1:])
            if anyOk == -1:
                sum += 1
                break
    else:
        sum += 1
    
print(sum)