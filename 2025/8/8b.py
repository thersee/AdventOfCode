import sys
from queue import PriorityQueue
from functools import cmp_to_key

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

class Cluster:
    def __init__(self, boxes):
        self.members = set()
        for b in boxes:
            self.members.add(b)

class JunctionBox:
    def __init__(self, x,y,z, clusters):
        self.x = x
        self.y = y
        self.z = z
        self.connected = Cluster([self])
        clusters.add(self.connected)

    def connect(self, otherBox, clusters: set):
        all = list()
        all.extend(self.connected.members)
        all.extend(otherBox.connected.members)
        if self.connected in clusters:
            clusters.remove(self.connected)
        if otherBox.connected in clusters:
            clusters.remove(otherBox.connected)
        #print(all)
        nc = Cluster(all)
        for b in all:
            b.connected = nc
        clusters.add(nc)

boxes = dict()
clusters = set()

for line in lines:
    x,y,z = line.split(',')
    box = JunctionBox(int(x), int(y), int(z), clusters)
    boxes[(x,y,z)] = box

distances = PriorityQueue()
for i in range(0, len(lines)):
    line1 = lines[i]
    for j in range(i, len(lines)):
        line2 = lines[j]
        if line1 != line2:
            x1,y1,z1 = line1.split(',')
            x2,y2,z2 = line2.split(',')
            dist = (int(x1)-int(x2))**2+(int(y1)-int(y2))**2+(int(z1)-int(z2))**2

            distances.put((dist, ((x1,y1,z1),(x2,y2,z2))))

while len(clusters) > 1:
    dist,nodes = distances.get()
    
    boxes[nodes[0]].connect(boxes[nodes[1]], clusters)
    #print(cluster.members)

print(int(nodes[0][0])*int(nodes[1][0]))