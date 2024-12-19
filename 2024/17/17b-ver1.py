import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

class Computer():
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c
    #0
    def divisionA(self, operand):
        factor = operand
        if operand == 4:
            factor = self.A
        elif operand == 5:
            factor = self.B
        elif operand == 6:
            factor = self.C
        self.A = int(self.A / 2**factor)
    #1
    def bitwiseOrWithInput(self, operand):
        self.B = self.B ^ operand
    #2
    def mod8(self, operand):
        number = operand
        if operand == 4:
            number = self.A
        elif operand == 5:
            number = self.B
        elif operand == 6:
            number = self.C
        self.B = number % 8
    #3
    def jump(self, operand):
        if self.A == 0:

            return -1 #do not jump, but increase pointer with 2
        else: 
            return operand # jump to here
    #4
    def bitwiseOrBC(self, operand):
        self.B = self.B ^ self.C
    #5  
    def printing(self, operand, alreadyPrinted):
        number = operand
        if operand == 4:
            number = self.A
        elif operand == 5:
            number = self.B
        elif operand == 6:
            number = self.C
        toPrint = str(number % 8)+ ','
        alreadyPrinted += toPrint
        # print(toPrint, end='')
        return alreadyPrinted

    #6
    def divisionB(self, operand):
        factor = operand
        if operand == 4:
            factor = self.A
        elif operand == 5:
            factor = self.B
        elif operand == 6:
            factor = self.C
        self.B = int(self.A / 2**factor)

    #7
    def divisionC(self, operand):
        factor = operand
        if operand == 4:
            factor = self.A
        elif operand == 5:
            factor = self.B
        elif operand == 6:
            factor = self.C
        self.C = int(self.A / 2**factor)

aStart = int(lines[0].split(': ')[1])
bStart = int(lines[1].split(': ')[1])
cStart = int(lines[2].split(': ')[1])
c = Computer(aStart,bStart,cStart)
programRaw = lines[4].split(': ')[1]
program = programRaw.split(',')
aValue = 0
alreadyPrinted = ''
run = True
while run and aValue < 1:
    c = Computer(aValue,bStart,cStart)
    alreadyPrinted = ''
    instructionPointer = 0
    runInner = True
    aValue += 1
    if aValue % 1000000 == 0:
        print(aValue)
    while instructionPointer < len(program) and runInner:
        instruction = int(program[instructionPointer])
        # print(instruction)
        input = int(program[instructionPointer + 1])
        if instruction == 0:
            c.divisionA(input)
            instructionPointer += 2
        elif instruction == 1:
            c.bitwiseOrWithInput(input)
            instructionPointer += 2
        elif instruction == 2:
            c.mod8(input)
            instructionPointer += 2
        elif instruction == 3:
            res = c.jump(input)
            if res == -1:
                instructionPointer += 2
            else:
                instructionPointer = res
        elif instruction == 4:
            c.bitwiseOrBC(input)
            instructionPointer += 2
        elif instruction == 5:
            alreadyPrinted = c.printing(input, alreadyPrinted)
            # print(alreadyPrinted)
            if alreadyPrinted == programRaw+',':
                print('tjoho')
                run = False
            elif not programRaw.startswith(alreadyPrinted):
                # print('nej nej nej')
                runInner = False
            instructionPointer += 2
        elif instruction == 6:
            c.divisionB(input)
            instructionPointer += 2
        elif instruction == 7:
            c.divisionC(input)
            instructionPointer += 2

print('result: ', aValue, alreadyPrinted)