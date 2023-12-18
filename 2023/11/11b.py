from collections import defaultdict

with open('11/input.txt') as f:
    lines = f.read().splitlines()


galaxies = list()
nonEmptyRows = list() 
nonEmptyCols = list() 
for row in range(0, len(lines)):
    for col in range(0, len(lines[0])):
        if lines[row][col] == '#':
            galaxies.append((row, col))
            nonEmptyRows.append(row)
            nonEmptyCols.append(col)

totalDist = 0
for first in galaxies:
    for second in galaxies:
        if first != second:
            # print("#"*50)
            dist = 0
            for i in range(first[0], second[0]):
                dist += 1
                if i not in nonEmptyRows:
                    # print('here')
                    dist += 999999
            for j in range(first[1], second[1]):
                dist += 1
                if j not in nonEmptyCols:
                    dist += 999999
            # print(dist, first, second)
            totalDist += dist

print(totalDist)
            
