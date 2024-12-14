with open('4/input.txt') as f:
    lines = f.read().splitlines()
    # lines = [int(x) for x in lines]

word = 'XMAS'
def checkAdj(letter, x,y, dirX, dirY):

    if x+dirX < len(lines[0]) and x+dirX >= 0 and y+dirY < len(lines) and y+dirY >= 0:
        otherLetter = lines[x+dirX][y+dirY]
        if letter == otherLetter and letter == 'S':
            return True
        elif letter == otherLetter:
            return checkAdj(word[word.find(letter)+1],x+dirX, y+dirY, dirX, dirY)
        else:
            return False
    else:
        return False    

totalXmas = 0
dirs = [(1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1), (0,1), (0,-1)]

for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if lines[i][j] == 'X':
            for dir in dirs:
                if checkAdj('M', i,j, dir[0], dir[1]):
                    # print(i,j,dir[0], dir[1])
                    totalXmas += 1

print(totalXmas)