import re

with open('3/input.txt') as f:
    lines = f.read().splitlines()
    # lines = [int(x) for x in lines]

sum = 0
for line in lines: 

    matches = re.findall('mul\(\d{1,3},\d{1,3}\)', line)
    for m in matches:
        newM = m[4:-1]
        nums = newM.split(',')
        sum += int(nums[0])*int(nums[1])

print(sum)


#155955228