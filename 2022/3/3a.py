
with open('3/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 11258
vals = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

priority = 0
for bag in lines:
    half = round(len(bag)/2)
    firstHalf = bag[0:half]
    secondHalf = bag[half:len(bag)]
    for thing in firstHalf:
        if thing in secondHalf:
            priority += vals.find(thing)+1
            break
print(priority)