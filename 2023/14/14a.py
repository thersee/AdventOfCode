with open('14/input.txt') as f:
    lines = f.read().splitlines()

stopRocks = [[-1] for i in range(len(lines[0]))]
slideRocks = [[] for i in range(len(lines[0]))]
for row, line in enumerate(lines):
    for col in range(0, len(line)):
        if line[col] == '#':
            stopRocks[col].append(row)
        elif line[col] == 'O':
            slideRocks[col].append(row)

def findLargestMin(row, listOfStops):
    smallest = 0
    for stop in listOfStops:
        if stop < row:
            smallest = stop
        elif stop > row:
            return smallest +1
    return smallest +1

# print(slideRocks)
totalSum = 0
for col, sliders in enumerate(slideRocks):
    stopRocksInt = stopRocks[col]
    # print("#"*50)
    # print(stopRocksInt)
    for slider in sliders:
        stopRocksInt.sort()
        newPos = findLargestMin(slider, stopRocksInt)
        # print(slider, col, newPos)
        totalSum += len(lines)-newPos
        stopRocksInt.append(newPos)
    # print(stopRocksInt)

print(totalSum)