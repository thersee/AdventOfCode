from collections import defaultdict
# fel svar (too low): 1529185
with open('7/input.txt') as f:
    lines = f.read().splitlines()
    #lines = [int(x) for x in lines] 11258

class Directory:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = list()
        self.fileSize = 0 #Non recursive
        self.totalFileSize = 0

dirs = list()
currentDir = Directory('/')
dirs.append(currentDir)

for i in range(0, len(lines)):
    line = lines[i]
    if line.startswith('$'):
        c = line.split(' ')
        if c[1] == 'cd':
            if c[2] == '..':
                currentDir = currentDir.parent
            else:
                for child in currentDir.children:
                    if child.name == c[2]:
                        currentDir = child
            #print(currentDir.name)
        elif c[1] == 'ls':
            while not i+1 >= len(lines) and not lines[i+1].startswith('$'):
                i += 1
                line = lines[i].split(' ')
                if line[0].startswith('dir'):
                    newDir = Directory(line[1])
                    dirs.append(newDir)
                    currentDir.children.append(newDir)
                    newDir.parent = currentDir
                else:
                    currentDir.fileSize += int(line[0])
                    currentDir.totalFileSize += int(line[0])
                    parent = currentDir.parent
                    while parent:
                        parent.totalFileSize += int(line[0])
                        parent = parent.parent

    i += 1


sum = 0
for directory in dirs:
    if directory.totalFileSize <= 100000:
        sum += directory.totalFileSize

print(sum)
