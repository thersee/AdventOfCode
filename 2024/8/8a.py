from collections import defaultdict

with open('8/input.txt') as f:
    lines = f.read().splitlines()

nodes = defaultdict(list)
antinodes = set()

for row in range(0, len(lines)):
    for col in range(0, len(lines[0])):
        antenna = lines[row][col] 
        if antenna != '.':
            nodes[antenna].append((row,col))
    
for antenna, indices in nodes.items():
    for i in range(0, len(indices)-1):
        ind1 = indices[i]
        for j in range(i+1, len(indices)):
            ind2 = indices[j]
            # print(antenna, ind1, ind2)
            v = (ind1[0]-ind2[0], ind1[1]-ind2[1])
            # print((ind2[0]-v[0], ind2[1]-v[1]))
            # print((ind1[0]+v[0], ind1[1]+v[1]))
            if (ind2[0]-v[0]) > -1 and (ind2[0]-v[0]) < len(lines) and  (ind2[1]-v[1]) > -1 and (ind2[1]-v[1]) < len(lines[0]):
                # print((ind2[0]-v[0], ind2[1]-v[1]), 1)
                antinodes.add((ind2[0]-v[0], ind2[1]-v[1]))
            if (ind1[0]+v[0]) > -1 and (ind1[0]+v[0]) < len(lines) and  (ind1[1]+v[1]) > -1 and (ind1[1]+v[1]) < len(lines[0]):
                # print((ind1[0]+v[0], ind1[1]+v[1]), 2)
                antinodes.add((ind1[0]+v[0], ind1[1]+v[1]))
print(len(antinodes))