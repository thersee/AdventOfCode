with open('10/input.txt') as f:
    lines = f.read().splitlines()

def isTrail(height, row, col, nodes):
    if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
        return set()
    if int(lines[row][col]) == height:
        # print(height, row, col)
        if height == 9:
            nodes.add((row,col))
            return nodes
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        totalTrails = set()
        for d in dirs:
            totalTrails.update(isTrail(height +1, row+d[0], col+d[1], nodes.copy()))
        return totalTrails
    return set()

trails = 0
for row in range(0, len(lines)):
    for col in range(0, len(lines[0])):
        if lines[row][col] == '0':
            trails += len(isTrail(0,row,col, set()))

print(trails)