import sys
import re

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

end = len(lines)-1
ops = lines[end]
opsArr = re.findall("[\\++\\*+]", ops)

lines = lines[:-1]
res = list()
for op in opsArr:
    if op == '+':
        res.append(0)
    else:
        res.append(1)
#print(res)
for line in lines:
    line = line
    nums = re.findall("\\d+", line)
    #print(nums)
    for i in range(len(nums)):
        if opsArr[i] == '+':
            res[i] += int(nums[i])
        else:
            res[i] *= int(nums[i])
    #print(res)
print(sum(res))