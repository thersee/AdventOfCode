import sys
from queue import Queue
from collections import defaultdict
from functools import cache

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()


    
def moveKeyPadRobot(currentPos, command):
    if command == 'A':
        print('clicking number '+ currentPos)
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
        print('clicking keypad '+ currentPos)
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
            
testMove = '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'

answer = 0
for line in lines:
    firstPos = line[0]
    endPos = line[1]

    toTest = Queue()
    toTest.put(('^', 'A', 'A', 'A', '', 0, 0))
    toTest.put(('>', 'A', 'A', 'A', '', 0, 0))
    toTest.put(('<', 'A', 'A', 'A', '', 0, 0))
    toTest.put(('v', 'A', 'A', 'A', '', 0, 0))
    toTest.put(('A', 'A', 'A', 'A', '', 0, 0))
    found = False
    alreadyVisited = list()
    while not found:
        node = toTest.get()
        if node[0:5] in alreadyVisited:
            continue
        else:
            alreadyVisited.append(node[0:5])
        toClick = node[0]
        # print("#"*20)
        # print(node)
        closestToMeBot = node[1]
        closestToKeyPadBot = node[2]
        keyPadBot = node[3]
        pressed = node[4]
        nbrOfPressed = node[5]
        increasedNbrOfPressed = nbrOfPressed + 1
        if toClick == 'A':
            if closestToMeBot == 'A':
                if closestToKeyPadBot == 'A':
                    # print(keyPadBot)
                    pressed += keyPadBot
                    if line == pressed:
                        found = True
                        answer += int(line[0:3])*increasedNbrOfPressed

                        print(increasedNbrOfPressed, int(line[0:3]))
                    if line.startswith(pressed):
                        # print(keyPadBot)
                        toTest.put(('^', closestToMeBot, closestToKeyPadBot, keyPadBot, pressed, increasedNbrOfPressed))
                        toTest.put(('>', closestToMeBot, closestToKeyPadBot, keyPadBot, pressed, increasedNbrOfPressed))
                        toTest.put(('<', closestToMeBot, closestToKeyPadBot, keyPadBot, pressed, increasedNbrOfPressed))
                        toTest.put(('v', closestToMeBot, closestToKeyPadBot, keyPadBot, pressed, increasedNbrOfPressed))
                        toTest.put(('A', closestToMeBot, closestToKeyPadBot, keyPadBot, pressed, increasedNbrOfPressed))

                else:
                    newKeypad = moveKeyPadRobot(keyPadBot, closestToKeyPadBot)
                    if newKeypad:
                        toTest.put(('^', closestToMeBot, closestToKeyPadBot, newKeypad, pressed, increasedNbrOfPressed))
                        toTest.put(('>', closestToMeBot, closestToKeyPadBot, newKeypad, pressed, increasedNbrOfPressed))
                        toTest.put(('<', closestToMeBot, closestToKeyPadBot, newKeypad, pressed, increasedNbrOfPressed))
                        toTest.put(('v', closestToMeBot, closestToKeyPadBot, newKeypad, pressed, increasedNbrOfPressed))
                        toTest.put(('A', closestToMeBot, closestToKeyPadBot, newKeypad, pressed, increasedNbrOfPressed))
            else:
                newctkBot = moveDirectionalRobot(closestToKeyPadBot, closestToMeBot)
                if newctkBot:
                    toTest.put(('^', closestToMeBot, newctkBot, keyPadBot, pressed, increasedNbrOfPressed))
                    toTest.put(('>', closestToMeBot, newctkBot, keyPadBot, pressed, increasedNbrOfPressed))
                    toTest.put(('<', closestToMeBot, newctkBot, keyPadBot, pressed, increasedNbrOfPressed))
                    toTest.put(('v', closestToMeBot, newctkBot, keyPadBot, pressed, increasedNbrOfPressed))
                    toTest.put(('A', closestToMeBot, newctkBot, keyPadBot, pressed, increasedNbrOfPressed))
                
        else:
            newctmBot = moveDirectionalRobot(closestToMeBot, toClick)
            if newctmBot:
                # print((newctmBot, closestToKeyPadBot, keyPadBot, pressed))
                toTest.put(('^', newctmBot, closestToKeyPadBot, keyPadBot, pressed, increasedNbrOfPressed))
                toTest.put(('>', newctmBot, closestToKeyPadBot, keyPadBot, pressed, increasedNbrOfPressed))
                toTest.put(('<', newctmBot, closestToKeyPadBot, keyPadBot, pressed, increasedNbrOfPressed))
                toTest.put(('v', newctmBot, closestToKeyPadBot, keyPadBot, pressed, increasedNbrOfPressed))
                toTest.put(('A', newctmBot, closestToKeyPadBot, keyPadBot, pressed, increasedNbrOfPressed))


print(answer)




