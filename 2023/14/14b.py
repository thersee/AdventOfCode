with open('14/input.txt') as f:
    lines = f.read().splitlines()

stopRocksNorth = [[-1, len(lines[0])] for i in range(len(lines[0]))]
stopRocksEast = [[-1, len(lines)] for i in range(len(lines))]
slideRocksNorth = [[] for i in range(len(lines))]
slideRocksEast = [[] for i in range(len(lines[0]))]

for row, line in enumerate(lines):
    for col in range(0, len(line)):
        if line[col] == '#':
            stopRocksNorth[col].append(row)
            stopRocksEast[row].append(col)
        elif line[col] == 'O':
            slideRocksNorth[col].append(row)

def findLargestMin(row, listOfStops):
    smallest = 0
    for stop in listOfStops:
        if stop < row:
            smallest = stop
        elif stop > row:
            return smallest +1
    return smallest +1

def findSmallestMax(row, listOfStops):
    largest = len(lines)
    for stop in listOfStops:
        if stop > row:
            largest = stop
        elif stop < row:
            return largest -1
    return largest - 1

oldSlideRocks = list()

for loop in range(0,1000000000):
    #North
    for col, sliders in enumerate(slideRocksNorth):
        stopRocksInt = stopRocksNorth[col].copy()
        sliders.sort()
        for slider in sliders:
            stopRocksInt.sort()
            newPos = findLargestMin(slider, stopRocksInt)
            stopRocksInt.append(newPos)
            slideRocksEast[newPos].append(col)

    # for i in range(0, 10):
    #     line = ''
    #     for j in range(0,10):
    #         if j in slideRocksEast[i]:
    #             line += 'O'
    #         elif j in stopRocksEast[i]:
    #             line += '#'
    #         else:
    #             line += '.'
    #     print(line)

    slideRocksNorth = [[] for i in range(len(lines[0]))]
    #West
    for row, sliders in enumerate(slideRocksEast):
        stopRocksInt = stopRocksEast[row].copy()
        sliders.sort()
        for slider in sliders:
            stopRocksInt.sort()
            newPos = findLargestMin(slider, stopRocksInt)
            # print(row, slider, newPos)
            stopRocksInt.append(newPos)
            slideRocksNorth[newPos].append(row)

    # print('')
    # print(slideRocksNorth)
    # for i in range(0, 10):
    #     line = ''
    #     for j in range(0,10):
    #         if i in slideRocksNorth[j]:
    #             line += 'O'
    #         elif i in stopRocksNorth[j]:
    #             line += '#'
    #         else:
    #             line += '.'
    #     print(line)

    slideRocksEast = [[] for i in range(len(lines[0]))]
    #South
    for col, sliders in enumerate(slideRocksNorth):
        stopRocksInt = stopRocksNorth[col].copy()
        sliders.sort(reverse=True)
        for slider in sliders:
            stopRocksInt.sort(reverse=True)
            newPos = findSmallestMax(slider, stopRocksInt)
            stopRocksInt.append(newPos)
            slideRocksEast[newPos].append(col)
    # print('')
    # for i in range(0, 10):
    #     line = ''
    #     for j in range(0,10):
    #         if j in slideRocksEast[i]:
    #             line += 'O'
    #         elif j in stopRocksEast[i]:
    #             line += '#'
    #         else:
    #             line += '.'
    #     print(line)

    slideRocksNorth = [[] for i in range(len(lines[0]))]
    totalSum = 0

    #East
    for row, sliders in enumerate(slideRocksEast):
        stopRocksInt = stopRocksEast[row].copy()
        sliders.sort(reverse=True) #Need to inverse sort
        for slider in sliders:
            stopRocksInt.sort(reverse=True) #Need to inverse sort
            newPos = findSmallestMax(slider, stopRocksInt)
            # print(row)
            totalSum += len(lines) - row
            stopRocksInt.append(newPos)
            slideRocksNorth[newPos].append(row)

    # print(totalSum)
    if(slideRocksNorth in oldSlideRocks):
        # print('Already been here, loop ' + str(loop+1))
        firstSeen = oldSlideRocks.index(slideRocksNorth)
        circle = loop - firstSeen
        # print(circle)
        if (1000000000-loop-1) % circle == 0:
            print(totalSum)
            break
    oldSlideRocks.append(slideRocksNorth)
    # print('')
    # for i in range(0, 10):
    #     line = ''
    #     for j in range(0,10):
    #         if i in slideRocksNorth[j]:
    #             line += 'O'
    #         elif i in stopRocksNorth[j]:
    #             line += '#'
    #         else:
    #             line += '.'
    #     print(line)
    

    # print(slideRocksNorth)
    slideRocksEast = [[] for i in range(len(lines[0]))]
    totalSum = 0

    #85077 too low