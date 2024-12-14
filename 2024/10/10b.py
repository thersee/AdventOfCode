with open('10/input.txt') as f:
    lines = f.read().splitlines()

def isTrail(height, row, col):
    if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
        return 0
    if int(lines[row][col]) == height:
        # print(height, row, col)
        if height == 9:
            return 1
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        totalTrails = 0
        for d in dirs:
            totalTrails += isTrail(height +1, row+d[0], col+d[1])
        return totalTrails
    return 0

trails = 0
for row in range(0, len(lines)):
    for col in range(0, len(lines[0])):
        if lines[row][col] == '0':
            trails += isTrail(0,row,col)

print(trails)