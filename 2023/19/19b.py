from queue import Queue

with open('19/input.txt') as f:
    lines = f.read().splitlines()

class Part():
    def __init__(self, xMin, xMax, mMin, mMax, aMin, aMax, sMin, sMax):
        self.xMin = xMin
        self.xMax = xMax
        self.mMin = mMin
        self.mMax = mMax
        self.aMin = aMin
        self.aMax = aMax
        self.sMin = sMin
        self.sMax = sMax

    def copy(self):
        return type(self)(self.xMin, self.xMax, self.mMin, self.mMax, self.aMin, self.aMax, self.sMin, self.sMax)

    def __str__(self):
        return '('+str(self.xMin)+', '+str(self.xMax)+') '+'('+str(self.mMin)+', '+str(self.mMax)+') '+'('+str(self.aMin)+', '+str(self.aMax)+') '+'('+str(self.sMin)+', '+str(self.sMax)+')'

    def get(self, letter):
        if letter == 'x':
            return (self.xMin, self.xMax)
        if letter == 'm':
            return (self.mMin, self.mMax)
        if letter == 'a':
            return (self.aMin, self.aMax)
        if letter == 's':
            return (self.sMin, self.sMax)

    def set(self, letter, min, max):
        if letter == 'x':
            self.xMin= min
            self.xMax=max
        if letter == 'm':
            self.mMin= min
            self.mMax=max
        if letter == 'a':
            self.aMin= min
            self.aMax=max
        if letter == 's':
            self.sMin= min
            self.sMax=max

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

accepted = list()

def evalRule(part, rule, index):
    r = rule[index]
    if r in ['A']:
        accepted.append(part)
        return
    elif r in ['R']:
        return
    gt = r.split('>')
    lt = r.split('<')
    if len(gt) > 1:
        val = part.get(gt[0])
        ins = gt[1].split(':')
        if val[0] <= int(ins[0]) and val[1] > int(ins[0]):
            newPart = part.copy()
            newPart.set(gt[0], int(ins[0])+1, val[1])
            if ins[1] in ['A']:
                accepted.append(newPart)
            elif ins[1] in ['R']:
                pass
            else:
                evalRule(newPart, rules[ins[1]], 0)
            otherPart = part.copy()
            otherPart.set(gt[0], val[0], int(ins[0]))
            evalRule(otherPart, rule, index+1)
        elif val[1] <= int(ins[0]):
            evalRule(part, rule, index+1)
        elif val[0] > int(ins[0]):
            if ins[1] in ['A']:
                accepted.append(part)
            elif ins[1] in ['R']:
                pass
            else:
                evalRule(part, rules[ins[1]], 0)
    elif len(lt) > 1:
        val = part.get(lt[0])
        ins = lt[1].split(':')
        if val[0] < int(ins[0]) and val[1] >= int(ins[0]):
            newPart = part.copy()
            newPart.set(lt[0], val[0], int(ins[0])-1)
            if ins[1] in ['A']:
                accepted.append(newPart)
            elif ins[1] in ['R']:
                pass
            else:
                evalRule(newPart, rules[ins[1]], 0)
            otherPart = part.copy()
            otherPart.set(lt[0], int(ins[0]), val[1])
            evalRule(otherPart, rule, index+1)
        elif val[0] >= int(ins[0]):
            evalRule(part, rule, index+1)
        elif val[1] < int(ins[0]):
            if ins[1] == 'A':
                accepted.append(part)
            elif ins[1] == 'R':
                pass
            else:
                evalRule(part, rules[ins[1]], 0)
    else:
        evalRule(part, rules[r], 0)

evalRule(Part(1,4000,1,4000,1,4000,1,4000), rules['in'], 0)

totalVarieties = 0
for acc in accepted:
    totalVarieties += (acc.xMax-acc.xMin+1)*(acc.mMax-acc.mMin+1)*(acc.aMax-acc.aMin+1)*(acc.sMax-acc.sMin+1)

print(totalVarieties)