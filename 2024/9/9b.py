
with open('9/input.txt') as f:
    lines = f.read().splitlines()


front = 0
line = lines[0]
back = len(line)-1
fileId = 0
checksum = 0
pos = 0
moved = set()

if back % 2 == 1:
    back -= 1
backNum = int(line[back])
 
while front <= back:
    if front not in moved:
        num = int(line[front]) #om den inte redan flyttats

        if front % 2 == 0:
            fileId = front/2
            if front == back:
                #hur gör man här då?
                for i in range(0, backNum):
                    # print(fileId)
                    checksum += pos*fileId
                    pos += 1
            else:
                for i in range(0, num):
                    # print(fileId)
                    checksum += pos*fileId
                    pos += 1
        else:
            num = int(line[front])
            go = True
            while num > 0 and go:
                # print("#", num)
                toMove = -1
                start = back
                while toMove == -1 and start > front:
                    if start not in moved:
                        testNum = int(line[start])
                        if testNum <= num:
                            toMove = start
                            moved.add(start)
                        else:
                            start -= 2
                    else:
                        start -= 2
                if toMove != -1:
                    # print("#",toMove)
                    num1 = int(line[toMove])
                    for i in range(0,num1):
                        fileId = toMove/2
                        # print(fileId)
                        checksum += fileId*pos
                        pos += 1
                    
                   
                    num = num - num1
                        #Kör igen
                        #minska num om det blev exakt...
                else: 
                    go = False
            # for i in range(0, num):
            #     # print('.')
            pos += num 
    else:
        num = int(line[front])
        # for i in range(0, num):
        #         print('.')
        pos += num 
    front += 1



print(checksum)