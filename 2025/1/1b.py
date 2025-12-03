import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

cur = 50
timesZero = 0
for line in lines:
    #print(cur)
    oldCur = cur
    d = line[0]
    num = int(line[1:])
 
    if d == 'L':
        for i in range(num):
            cur -= 1
            if cur == -1:
                cur += 100
            if cur == 0:
                timesZero += 1

        #print("-"+str(num))
    else:
        for i in range(num):
            cur += 1
            if cur == 100:
                cur -= 100
            if cur == 0:
                timesZero += 1
        #cur += num
        #print("+"+str(num))
    #print(cur)



    

print(timesZero)


#5657