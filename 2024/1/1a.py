
with open('1/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines]

list1 = []
list2 = []
sum = 0
for i in range(0, len(lines)):
    line = lines[i]
    nums = line.split('   ')
    print(nums)
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))

list1.sort()
list2.sort()
for j in range(0,len(list1)):
    sum += abs(list1[j]-list2[j])


    

print(sum)
