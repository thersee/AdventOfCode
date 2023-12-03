with open('3/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines]
def isAdjacentToSymbol(row, startColumn, endColumn):
    rows = [row-1, row, row +1]
    for r in rows:
        for c in range(startColumn, endColumn):
            # print(startColumn)
            if r > -1 and r < len(lines) and c > -1 and c < len(lines[r]):
                # print(r,c, lines[r][c])
                if lines[r][c] != '.' and not lines[r][c].isdigit():
                    return True
    return False

totalSum = 0

for index, line in enumerate(lines):
    number = ''
    startColumn = -1
    for col in range(0, len(line)):
        if line[col].isdigit():
            number = number + line[col]
            if startColumn == -1:
                startColumn = col
        elif number.isdigit():
            # print("#"*50)
            # print(number)
            if isAdjacentToSymbol(index, startColumn-1, col+1):
                # print("is counted")
                totalSum = totalSum + int(number)
            # else:
            #     # print("#"*50)
            #     # print(number, index, startColumn)
            #     print("is not counted")
            number = ''
            startColumn = -1
        # print(col, number)
        if (col == len(line)-1 and number.isdigit()):
            if isAdjacentToSymbol(index, startColumn-1, col+1):
                # print("is counted")
                totalSum = totalSum + int(number)
            # else:
            #     print("#"*50)
            #     print(number, index, startColumn)
            #     print("is not counted")

print(totalSum)