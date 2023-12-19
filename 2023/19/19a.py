with open('19/input.txt') as f:
    lines = f.read().splitlines()

class Part():
    def __init__(self, x, m,a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def get(self, letter):
        if letter == 'x':
            return self.x
        if letter == 'm':
            return self.m
        if letter == 'a':
            return self.a
        if letter == 's':
            return self.s

    def sum(self):
        return self.x+self.m+self.a+self.s

rules = dict()
parts = list()

line = lines[0]
index = 0
while line != '':
    first = line.split('{')
    name = first[0]
    instructions = first[1][:-1].split(',')
    rules[name] = instructions
    index += 1
    line = lines[index]

for line in lines[index+1:]:
    values = line.split(',')
    x = int(values[0][1:].split('=')[-1])
    m = int(values[1].split('=')[-1])
    a = int(values[2].split('=')[-1])
    s = int(values[3][:-1].split('=')[-1])
    parts.append(Part(x,m,a,s))

def evalRule(part, rule, index):
    r = rule[index]
    if r in ['R', 'A']:
        return r
    gt = r.split('>')
    lt = r.split('<')
    if len(gt) > 1:
        val = part.get(gt[0])
        ins = gt[1].split(':')
        if val > int(ins[0]):
            if ins[1] in ['A', 'R']:
                return ins[1]
            else:
                return evalRule(part, rules[ins[1]], 0)
        else:
            return evalRule(part, rule, index +1)
    elif len(lt) > 1:
        val = part.get(lt[0])
        ins = lt[1].split(':')
        if val < int(ins[0]):
            if ins[1] in ['A', 'R']:
                return ins[1]
            else:
                return evalRule(part, rules[ins[1]], 0)
        else:
            return evalRule(part, rule, index +1)
    else:
        return evalRule(part, rules[r], 0)

totalSum = 0
for part in parts:
    accRej = evalRule(part, rules['in'], 0)
    if accRej == 'A':
        totalSum += part.sum()

print(totalSum)