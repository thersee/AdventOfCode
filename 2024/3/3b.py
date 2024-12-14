import re

with open('3/input.txt') as f:
    lines = f.read().splitlines()

sum = 0
shouldMul = True
for line in lines:
    r1 = re.escape(r"don't())")
    r2 = re.escape(r"do())")
    nextMatch = re.findall("(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))",line)
    for match in nextMatch:
        if match == "don't()":
            shouldMul = False
        elif match == "do()":
            shouldMul = True
        elif shouldMul:
            newM = match[4:-1]
            nums = newM.split(',')
            sum += int(nums[0])*int(nums[1])
   
print(sum)
