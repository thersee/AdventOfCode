import sys
import re

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

def doMath(nums, op, res):
    if op == '+':
        res += sum(nums)
    else:
        a = 1
        for n in nums:
            a *= n
        res += a
    return res

end = len(lines)-1
ops = lines[end]
opsArr = re.findall("[\\++\\*+]", ops)

res = 0

totalLength = len(ops)
nums = list()
doMaths = False
for i in range(totalLength):
    ind = totalLength -i-1
    num = ''
    for line in lines:
        if line[ind] in ['+', '*']:
            doMaths = True
        else:
            num += line[ind]
    
    if num.strip():
        nums.append(int(num))
    if doMaths:
        res = doMath(nums, line[ind], res)
        nums = list()
        doMaths = False

print(res)
