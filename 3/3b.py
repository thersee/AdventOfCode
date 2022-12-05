
with open('3/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 11258
vals = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

priority = 0
i = 0
while i < len(lines):
    bag1 = lines[i]
    bag2 = lines[i+1]
    bag3 = lines[i+2]
    print(bag1)
    for val in vals:
        if bag1.find(val) != -1 and bag2.find(val)!= -1 and bag3.find(val) != -1:
            priority += vals.find(val) + 1
    i += 3
print(priority)