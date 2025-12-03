import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

tot = 0
for line in lines:
    max = ['0']*12
    for i in range(len(line)):
        s = len(max)-(len(line)-i)
        if s < 0:
            s = 0
        for j in range(min(s, len(max)), len(max)):
            if line[i] > max[j]:
                orig = max[:j] if max[:j] else []
                orig.extend([line[i]])
                orig.extend(['0'] * (len(max)-1-j))
                max = orig
                break
    tot += int(''.join(max))

print(tot)