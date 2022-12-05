
with open('4/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 11258

sum = 0
for line in lines:
    vals = line.split(',')
    first = vals[0]
    f1, f2 = first.split('-')
    second = vals[1]
    s1, s2 = second.split('-')
    f1 = int(f1)
    f2 = int(f2)
    s1 = int(s1)
    s2 = int(s2)
    if (f1 >= s1 and f1 <= s2 and f2 >= s1 and f2 <= s2) or (s1 >= f1 and s1 <= f2 and s2 >= f1 and s2 <= f2):
        sum += 1

print(sum)
