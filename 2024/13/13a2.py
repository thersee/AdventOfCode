from collections import defaultdict
import numpy as np

with open('13/input.txt') as f:
    lines = f.read().splitlines()

def GCD(a, b):
    if a == b:
        return a
    if a > b:
        return GCD(a-b, b)
    else:
        return GCD(a, b-a)

def solveProblemWithGCD(a,b,prize):
    firstGCD = GCD(a[0], b[0])
    secondGCD = GCD(a[1], b[1])
    print(firstGCD, secondGCD)

print(solveProblemWithGCD((94,34), (22,67), [4098, 6834]))

# totalCost = 0
# for problem in range(0, len(lines), 4):
#     a = lines[problem].split(': ')[1].split(', ')
#     a = (a[0].split('+')[1], a[1].split('+')[1])
#     b = lines[problem+1].split(': ')[1].split(', ')
#     b = (b[0].split('+')[1], b[1].split('+')[1])
#     prize = lines[problem+2].split(': ')[1].split(', ')
#     prize = [int(prize[0].split('=')[1]), int(prize[1].split('=')[1])]
#     # print(a,b,prize)
#     sol = solveProblemWithGCD(a, b, prize)
#     # print(sol)
#     if sol:
#         thisCost = sol[0]*3+sol[1]
#         # print(thisCost)
#         totalCost += thisCost

# print(totalCost)
# # 23326 too low
# # 35653 too low