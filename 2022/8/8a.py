from collections import defaultdict

with open('8/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 

nbrVisible = set() #Lägg till kanter
for i in range(0,len(lines[0])):
    maxHeighti = "-1"
    for j in range(0, len(lines)):
        if lines[i][j] > maxHeighti:
            #print(lines[i][j])
            maxHeighti = lines[i][j]
            nbrVisible.add((i,j))
    maxHeighti = "-1"
    for k in range(0, len(lines)):
        if lines[i][len(lines)-1-k] > maxHeighti:
            #print(lines[i][len(lines)-1-k])
            maxHeighti = lines[i][len(lines)-1-k]
            nbrVisible.add((i,len(lines)-1-k))
    

for i in range(0, len(lines)):
    maxHeighti = "-1"
    for j in range(0,len(lines[0])):
        if lines[j][i] > maxHeighti:
            #print(lines[j][i])
            maxHeighti = lines[j][i]
            nbrVisible.add((j,i))
    maxHeighti = "-1"
    for k in range(0,len(lines[0])):
        if lines[len(lines)-1-k][i] > maxHeighti:
            #print(lines[len(lines)-1-k][i] )
            maxHeighti = lines[len(lines)-1-k][i]
            nbrVisible.add((len(lines)-1-k,i))
    

print(len(nbrVisible))