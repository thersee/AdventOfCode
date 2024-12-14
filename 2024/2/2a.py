with open('2/input.txt') as f:
    lines = f.read().splitlines()
    # lines = [int(x) for x in lines]

sum = 0
for i in range(0, len(lines)):
    line = lines[i].split(' ')
    line = [int(x) for x in line]
    inc = line[1] - line[0] > 0
    ok = True
    for j in range(0, len(line)-1):
        if line[j+1] - line[j] > 0 and inc:
            if line[j+1] - line[j] > 3:
                ok = False
        elif line[j+1] - line[j] < 0 and not inc:
            if line[j+1] - line[j] < -3:
                ok = False
        else:
            ok = False
        
        if not ok:
            break
    if ok:
        sum += 1

print(sum)