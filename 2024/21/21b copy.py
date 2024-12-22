import sys
from queue import Queue, PriorityQueue
from collections import defaultdict
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()


    
def moveKeyPadRobot(currentPos, command):
    if command == 'A':
        # print('clicking number '+ currentPos)
        pass
    elif currentPos == 'A':
        if command == '^':
            currentPos = '3'
            return currentPos
        elif command == '<':
            currentPos = '0'
            return currentPos
        else:
            return None
    elif currentPos == '0':
        if command == '^':
            currentPos = '2'
            return currentPos
        elif command == '>':
            currentPos = 'A'
            return currentPos
        else:
            return None
    elif currentPos == '1':
        if command == '^':
            currentPos = '4'
            return currentPos
        elif command == '>':
            currentPos = '2'
            return currentPos
        else:
            return None
    elif currentPos == '2':
        if command == '^':
            currentPos = '5'
            return currentPos
        elif command == '>':
            currentPos = '3'
            return currentPos
        elif command == '<':
            currentPos = '1'
            return currentPos
        elif command == 'v':
            currentPos = '0'
            return currentPos
    elif currentPos == '3':
        if command == '^':
            currentPos = '6'
            return currentPos
        elif command == '<':
            currentPos = '2'
            return currentPos
        elif command == 'v':
            currentPos = 'A'
            return currentPos
        else:
            return None
    elif currentPos == '4':
        if command == '^':
            currentPos = '7'
            return currentPos
        elif command == '>':
            currentPos = '5'
            return currentPos
        elif command == 'v':
            currentPos = '1'
            return currentPos
        else:
            return None
    elif currentPos == '5':
        if command == '^':
            currentPos = '8'
            return currentPos
        elif command == '>':
            currentPos = '6'
            return currentPos
        elif command == 'v':
            currentPos = '2'
            return currentPos
        elif command == '<':
            currentPos = '4'
            return currentPos
    elif currentPos == '6':
        if command == '^':
            currentPos = '9'
            return currentPos
        elif command == 'v':
            currentPos = '3'
            return currentPos
        elif command == '<':
            currentPos = '5'
            return currentPos
        else:
            return None
    elif currentPos == '7':
        if command == 'v':
            currentPos = '4'
            return currentPos
        elif command == '>':
            currentPos = '8'
            return currentPos
        else:
            return None
    elif currentPos == '8':
        if command == 'v':
            currentPos = '5'
            return currentPos
        elif command == '>':
            currentPos = '9'
            return currentPos
        elif command == '<':
            currentPos = '7'
            return currentPos
        else:
            return None
    elif currentPos == '9':
        if command == 'v':
            currentPos = '6'
            return currentPos
        elif command == '<':
            currentPos = '8'
            return currentPos
        else:
            return None

    
def moveDirectionalRobot(currentPos, command):
    if command == 'A':
        # print('clicking keypad '+ currentPos)
        pass
    elif currentPos == 'A':
        if command == '<':
            currentPos = '^'
            return currentPos
        elif command == 'v':
            currentPos = '>'
            return currentPos
        else:
            return None
    if currentPos == '^':
        if command == '>':
            currentPos = 'A'
            return currentPos
        elif command == 'v':
            currentPos = 'v'
            return currentPos
        else:
            return None
    if currentPos == '<':
        if command == '>':
            currentPos = 'v'
            return currentPos
        else:
            return None
    if currentPos == 'v':
        if command == '>':
            currentPos = '>'
            return currentPos
        elif command == '<':
            currentPos = '<'
            return currentPos
        elif command == '^':
            currentPos = '^'
            return currentPos
        else:
            return None
    if currentPos == '>':
        if command == '<':
            currentPos = 'v'
            return currentPos
        elif command == '^':
            currentPos = 'A'
            return currentPos
        else:
            return None

def moveAround(click, closestToMeBot, closestToKeyPadBot, keyPadBot):
    if click == 'A':
        if closestToMeBot == 'A':
            closestToKeyPadBot
            if closestToKeyPadBot == 'A':
                print(keyPadBot)
                return (closestToMeBot, closestToKeyPadBot, keyPadBot)
            else:
                newKeypad = moveKeyPadRobot(keyPadBot, closestToKeyPadBot)
                if newKeypad:
                    return (closestToMeBot, closestToKeyPadBot, newKeypad)
                else:
                    print('first', keyPadBot, closestToKeyPadBot)
                
        else:
            newctkBot = moveDirectionalRobot(closestToKeyPadBot, closestToMeBot)
            if newctkBot:
                return (closestToMeBot, newctkBot, keyPadBot)
            else:
                print('second', closestToKeyPadBot, closestToMeBot)
            
    else:
        newctmBot = moveDirectionalRobot(closestToMeBot, click)
        if newctmBot:
            return (newctmBot, closestToKeyPadBot, keyPadBot)
        else:
            print('third', closestToMeBot, click)

costFirstDirectional = defaultdict(int)
buttons = ['A', '<', '>', 'v', '^']
for start in buttons:
    for goal in buttons:
        found = False
        toTest = Queue()
        alreadyVisited = []
        toTest.put(( 'A' ,start, ''))
        toTest.put(( 'v' ,start, ''))
        toTest.put(( '<' ,start, ''))
        toTest.put(( '>' ,start, ''))
        toTest.put(( '^' ,start, ''))

        while not found:
            node = toTest.get()
            if node in alreadyVisited:
                continue
            alreadyVisited.append(node)
            newAlreadyPressed = node[2] + node[0]
            if node[1] == goal and node[0] == 'A':
                found = True
                # print('from:', start, 'to:', goal, 'path:',newAlreadyPressed)
                costFirstDirectional[(start, goal)] = newAlreadyPressed
            else:
                newPos = moveDirectionalRobot(node[1], node[0])
                if newPos:
                    toTest.put( ('A' ,newPos, newAlreadyPressed))
                    toTest.put( ('v' ,newPos, newAlreadyPressed))
                    toTest.put( ('<' ,newPos, newAlreadyPressed))
                    toTest.put( ('>' ,newPos, newAlreadyPressed))
                    toTest.put( ('^' ,newPos, newAlreadyPressed))

costPrevious = costFirstDirectional
for i in range(1):
    print(i)
    thisCost = defaultdict(int)
    for start in buttons:
        for goal in buttons:
            found = False
            toTest = PriorityQueue()
            alreadyVisited = []
            toTest.put((len(costPrevious[('A', 'A')]), 'A' , start, costPrevious[('A', 'A')]))
            toTest.put((len(costPrevious[('A', 'v')]),  'v' , start, costPrevious[('A', 'v')]))
            toTest.put((len(costPrevious[('A', '<')]), '<' , start, costPrevious[('A', '<')]))
            toTest.put((len(costPrevious[('A', '>')]), '>' , start, costPrevious[('A', '>')]))
            toTest.put((len(costPrevious[('A', '^')]), '^' , start, costPrevious[('A', '^')]))

            while not found:
                node = toTest.get()
                if node[1:] in alreadyVisited:
                    continue
                alreadyVisited.append(node[1:])
                if node[2] == goal and node[1] == 'A':
                    found = True
                    costToClick = node[3]
                    # print('from:', start, 'to:', goal, 'path:',costToClick)
                    thisCost[(start, goal)] = costToClick
                else:
                    newPos = moveDirectionalRobot(node[2], node[1])
                    if newPos:
                        toTest.put( (len(node[3]+costPrevious[(node[1], 'A')]), 'A' ,newPos, node[3]+costPrevious[(node[1], 'A')]))
                        toTest.put( (len(node[3]+costPrevious[(node[1], 'v')]), 'v' ,newPos, node[3]+costPrevious[(node[1], 'v')]))
                        toTest.put( (len(node[3]+costPrevious[(node[1], '<')]), '<' ,newPos, node[3]+costPrevious[(node[1], '<')]))
                        toTest.put( (len(node[3]+costPrevious[(node[1], '>')]), '>' ,newPos, node[3]+costPrevious[(node[1], '>')]))
                        toTest.put( (len(node[3]+costPrevious[(node[1], '^')]), '^' ,newPos, node[3]+costPrevious[(node[1], '^')]))

    costPrevious = thisCost


keyPadButtons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']
thisCost = defaultdict(int)
for start in keyPadButtons:
    for goal in keyPadButtons:
        found = False
        toTest = PriorityQueue()
        alreadyVisited = []
        toTest.put((len(costPrevious[('A', 'A')]), 'A' , start, costPrevious[('A', 'A')]))
        toTest.put((len(costPrevious[('A', 'v')]),  'v' , start, costPrevious[('A', 'v')]))
        toTest.put((len(costPrevious[('A', '<')]), '<' , start, costPrevious[('A', '<')]))
        toTest.put((len(costPrevious[('A', '>')]), '>' , start, costPrevious[('A', '>')]))
        toTest.put((len(costPrevious[('A', '^')]), '^' , start, costPrevious[('A', '^')]))

        while not found:
            node = toTest.get()
            # print(node)
            if node[1:] in alreadyVisited:
                continue
            alreadyVisited.append(node[1:])
            if node[2] == goal and node[1] == 'A':
                found = True
                costToClick = node[3]
                # print('from:', start, 'to:', goal, 'path:',costToClick)
                thisCost[(start, goal)] = costToClick
            else:
                newPos = moveKeyPadRobot(node[2], node[1])
                if newPos:
                    toTest.put( (len(node[3]+costPrevious[(node[1], 'A')]), 'A' ,newPos, node[3]+costPrevious[(node[1], 'A')]))
                    toTest.put( (len(node[3]+costPrevious[(node[1], 'v')]), 'v' ,newPos, node[3]+costPrevious[(node[1], 'v')]))
                    toTest.put( (len(node[3]+costPrevious[(node[1], '<')]), '<' ,newPos, node[3]+costPrevious[(node[1], '<')]))
                    toTest.put( (len(node[3]+costPrevious[(node[1], '>')]), '>' ,newPos, node[3]+costPrevious[(node[1], '>')]))
                    toTest.put( (len(node[3]+costPrevious[(node[1], '^')]), '^' ,newPos, node[3]+costPrevious[(node[1], '^')]))

answer = 0
for line in lines:
    totalCost = thisCost[('A', line[0])]
    for i  in range(len(line)-1):
        totalCost += thisCost[line[i], line[i+1]]
    print(len(totalCost))
    answer += int(line[0:3])*len(totalCost)
print(answer)

