
with open('9/input.txt') as f:
    lines = f.read().splitlines()


front = 0
line = lines[0]
back = len(line)-1
fileId = 0
checksum = 0
pos = 0

if back % 2 == 1:
    back -= 1
backNum = (int(line[back]), int(line[back]))

while front <= back:
    num = int(line[front])

    if front % 2 == 0:
        fileId = front/2
        if front == back:
            for i in range(0, backNum[1]):
                # print(fileId)
                checksum += pos*fileId
                pos += 1
        else:
            for i in range(0, num):
                # print(fileId)
                checksum += pos*fileId
                pos += 1
    else:
        for i in range(0,num):
            fileId = back/2
            if backNum[1] > 0:
                # print(fileId)
                checksum += fileId*pos
                backNum = (backNum[0], backNum[1]-1)
            else:
                back -= 2
                if back > front:
                    fileId = back/2
                    backNum = (int(line[back]), int(line[back]))
                    # print(fileId)
                    checksum += fileId*pos
                    backNum = (backNum[0], backNum[1]-1)
            pos += 1
    front += 1

print(checksum)