import sys, re

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

sumInvalid = 0
for line in lines:
    parts = line.split(',')
    for part in parts:
        interval = part.split('-')

        if interval == ['']:
            continue
        for i in range(int(interval[0]), int(interval[1])+1):
            s = str(i)
            match = re.fullmatch("(?P<first>([0-9])*)(?P=first)+",s)
            if match:
                #print(i)
                sumInvalid += i


            #print(s)
            # l = len(s)
            # invalids = set()
            # for j in range(1,int(l/2)+1):
            #     #print(l,j)
            #     if l % j == 0:
            #         #print(j)
            #         parts = int(l/j)
            #         lengths = int(l/parts)
            #         isValid = True
            #         for k in range(parts-1):
            #             #print(k)
            #             if s[lengths*k:lengths*(k+1)] != s[lengths*(k+1):lengths*(k+2)]:
            #                 #print(s[lengths*k:lengths*(k+1)], s[lengths*(k+1):lengths*(k+2)])
            #                 isValid = False
            #         if isValid:
            #             #print(i)
            #             invalids.add(i)
            # for inv in invalids:
            #     sumInvalid += inv

print(sumInvalid)

#58961152806