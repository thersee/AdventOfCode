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
        # print('divA', end='')
        if operand == 4:
            # print('A', self.A, end='')
            factor = self.A
        elif operand == 5:
            # print('B', self.B, end='')
            factor = self.B
        elif operand == 6:
            # print('C', self.C, end='')
            factor = self.C
        # print('divA', self.A, 2**factor, end='')
        self.A = int(self.A / 2**factor)
        # print('after', self.A, 2**factor)
    #1
    def bitwiseOrWithInput(self, operand):
        # print('xor op', self.B, end='')
        self.B = self.B ^ operand
        # print('after:', self.B)
    #2
    def mod8(self, operand):
        number = operand
        # print('mod8', number, end='')
        if operand == 4:
            # print('A', self.A, end='')
            number = self.A
        elif operand == 5:
            # print('B', self.B, end='')
            number = self.B
        elif operand == 6:
            # print('C', self.C, end='')
            number = self.C
        self.B = number % 8
        # print(' ', number, self.B)
    #3
    def jump(self, operand):
        if self.A == 0:
            # print('no jump')
            return -1 #do not jump, but increase pointer with 2
        else: 
            # print('jump', operand, self.A)
            return operand # jump to here
    #4
    def bitwiseOrBC(self, operand):
        # print('xorBC', self.B, self.C)
        self.B = self.B ^ self.C
    #5  
    def printing(self, operand, toPrint):
        number = operand
        # print('print', end='')
        if operand == 4:
            # print('A', self.A, end='')
            number = self.A
        elif operand == 5:
            # print('B', self.B, end='')
            number = self.B
        elif operand == 6:
            # print('C', self.C, end='')
            number = self.C
        # print('number', end='')
        toPrint.append(str(number % 8))
        return toPrint
        # print(str(number % 8)+ ',', end='')

    #6
    def divisionB(self, operand):
        factor = operand
        factor = operand
        # print('divB', end='')
        if operand == 4:
            # print('A', self.A, end='')
            factor = self.A
        elif operand == 5:
            # print('B', self.B, end='')
            factor = self.B
        elif operand == 6:
            # print('C', self.C, end='')
            factor = self.C
        # print('divA', self.A, 2**factor, end='')
        self.B = int(self.A / 2**factor)
        # print('after', self.B, 2**factor)

    #7
    def divisionC(self, operand):
        factor = operand
        factor = operand
        # print('divC', end='')
        if operand == 4:
            # print('A', self.A, end='')
            factor = self.A
        elif operand == 5:
            # print('B', self.B, end='')
            factor = self.B
        elif operand == 6:
            # print('C', self.C, end='')
            factor = self.C
        # print('divC', self.A, 2**factor, end='')
        self.C = int(self.A / 2**factor)
        # print('after', self.C, 2**factor)

originalProgram = lines[4].split(': ')[1]
program = originalProgram.split(',')

def runProgram(aStart, bStart, cStart):
    c = Computer(aStart,bStart,cStart)
    # program = '7,7,0'
    instructionPointer = 0
    toPrint = []

    while instructionPointer < len(program):
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
            # print('instructionPointer', instructionPointer)
        elif instruction == 4:
            c.bitwiseOrBC(input)
            instructionPointer += 2
        elif instruction == 5:
            toPrint = c.printing(input, toPrint)
            instructionPointer += 2
        elif instruction == 6:
            c.divisionB(input)
            instructionPointer += 2
        elif instruction == 7:
            c.divisionC(input)
            instructionPointer += 2
    return toPrint

thisCouldBeIt = [(5, 15)]
possibleSolutions = []
while len(thisCouldBeIt):
    item = thisCouldBeIt.pop(0)
    toTest = item[0]
    index = item[1]
    res = runProgram(toTest,0,0)
    if index == 0:
        if res == program:
            possibleSolutions.append(toTest)
    if res == program[index:]:
        for j in range(8):
            thisCouldBeIt.append((toTest*8+j, index-1))
possibleSolutions.sort()
print(possibleSolutions)