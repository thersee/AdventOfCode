from collections import defaultdict

with open('5/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 11258

allCrates = defaultdict(list)
for crates in lines:
    if crates.startswith('move'):
        words = crates.split(' ')
        nbr = int(words[1])
        fromCrate = int(words[3])
        toCrate = int(words[5])
        for i in range(0,nbr):
            toMove =allCrates.get(fromCrate).pop(0)
            allCrates.get(toCrate).insert(0, (toMove))
    elif crates.startswith(' 1'):
        pass
    else:
        i = 0
        stack = 1
        while i < len(crates):
            crate = crates[i+1:i+2]
            if crate != ' ':
                allCrates[stack].append(crate)
            stack += 1
            i += 4

password = ''
for i in range(1, len(allCrates)+1):
    password += allCrates.get(i).pop(0)

print(password)