from collections import defaultdict

with open('8/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 

def seeUp(i, j):
    height = lines[i][j]
    visibility = 0
    i -= 1
    while i > -1:
        if lines[i][j] < height:
            visibility += 1
        else:
            visibility +=1 
            return visibility
        i -= 1
    return visibility

def seeDown(i,j):
    height = lines[i][j]
    visibility = 0
    i += 1
    while i < len(lines[0]):
        if lines[i][j] < height:
            visibility += 1
        else:
            visibility +=1 
            return visibility
        i += 1
    return visibility

def seeLeft(i,j):
    height = lines[i][j]
    visibility = 0
    j -= 1
    while j > -1:
        if lines[i][j] < height:
            visibility += 1
        else:
            visibility +=1 
            return visibility
        j -= 1
    return visibility


def seeRight(i,j):
    height = lines[i][j]
    visibility = 0
    j += 1
    while j < len(lines):
        if lines[i][j] < height:
            visibility += 1
        else:
            visibility +=1 
            return visibility
        j += 1
    return visibility

bestScore = 0
for i in range(0,len(lines[0])):
    for j in range(0, len(lines)):
        score = seeRight(i, j)*seeDown(i,j)*seeUp(i,j)*seeLeft(i,j)
        if score > bestScore:
            bestScore = score

print(bestScore)
