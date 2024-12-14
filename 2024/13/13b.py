from collections import defaultdict
import numpy as np

with open('13/input.txt') as f:
    lines = f.read().splitlines()


def solveProblem(a,b,prize):
    A = [[int(a[0]), int(b[0])], [int(a[1]), int(b[1])]]
    
    solution = np.linalg.solve(A, prize)
    print("#"*50)
    print(solution)
    # print(str(solution[0]),str(solution[1]), abs(round(solution[1])-solution[1]))
    if abs(round(solution[0])-solution[0])<0.01 and abs(round(solution[1])-solution[1])<0.01 :
        print([round(solution[0]), round(solution[1])])
        return [round(solution[0]), round(solution[1])]
    return []

totalCost = 0
for problem in range(0, len(lines), 4):
    a = lines[problem].split(': ')[1].split(', ')
    a = (a[0].split('+')[1], a[1].split('+')[1])
    b = lines[problem+1].split(': ')[1].split(', ')
    b = (b[0].split('+')[1], b[1].split('+')[1])
    prize = lines[problem+2].split(': ')[1].split(', ')
    prize = [int(prize[0].split('=')[1])+10000000000000, int(prize[1].split('=')[1])+10000000000000]
    # print(a,b,prize)
    sol = solveProblem(a, b, prize)
    # print(sol)
    if sol:
        thisCost = sol[0]*3+sol[1]
        # print(thisCost)
        totalCost += thisCost

print(totalCost)
# too low 51075054106437 b