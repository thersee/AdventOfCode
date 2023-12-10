with open('20/input.txt') as f:
    lines = f.read().splitlines()

class ListNode:
    def __init__(self, prev, next, val, startVal):
        self.prev = prev
        self.next = next
        self.val = val
        self.startVal = startVal

    def shiftRight(self):
        oldPrev = self.prev
        oldNext = self.next
        oldNextNext = self.next.next
        oldPrev.next = oldNext #ok
        oldNext.prev = oldPrev #ok
        self.next = oldNextNext #ok
        self.prev = oldNext #ok
        oldNext.next = self
        oldNextNext.prev = self
    
    def shiftLeft(self):
        oldPrev = self.prev
        oldNext = self.next
        oldPrevPrev = self.prev.prev
        oldPrev.next = oldNext
        oldNext.prev = oldPrev
        oldPrev.prev = self
        self.next = oldPrev
        self.prev = oldPrevPrev
        oldPrevPrev.next = self

    def printList(self):
        print(self.startVal)
        next = self.next
        while next != self:
            print(next.startVal)
            next = next.next

    def getVal(self):
        index = 1
        val = 0
        node = self.next
        while index <= 3000:
            if index == 1000 or index == 2000 or index == 3000:
                val += node.startVal
            node = node.next
            index += 1
        return val

allNodesInOrder = list()
prev = None
nodeZero = None

for line in lines:
    node = ListNode(prev, None, int(line)*811589153%(len(lines)-1), int(line)*811589153)
    if prev:
        node.prev = prev
        prev.next = node
    allNodesInOrder.append(node)
    prev = node
    if line == '0':
        nodeZero = prev

allNodesInOrder[0].prev = prev
prev.next = allNodesInOrder[0]

iterations = len(allNodesInOrder)*10
for j in range(0, iterations):
    node = allNodesInOrder[j%len(allNodesInOrder)]
    if node.val > 0:
        for i in range(0,node.val):
            node.shiftRight()
    else:
         for i in range(0, abs(node.val)):
            node.shiftLeft()

print("######")
#nodeZero.printList()
print(nodeZero.getVal())