from queue import Queue

with open('20/input.txt') as f:
    lines = f.read().splitlines()

class FlipFlop:
    def __init__(self, sendTo, name):
        self.name = name
        self.on = False
        self.sendTo = sendTo

    def getSignal(self, pulse, fromNode=''):
        pulsesToSend = list()
        if pulse == 'low':
            if self.on == True:
                self.on = False
                for n in self.sendTo:
                    pulsesToSend.append((n, 'low', self.name))
            elif self.on == False:
                self.on = True
                for n in self.sendTo:
                    pulsesToSend.append((n, 'high', self.name))
        return pulsesToSend

class Conjunction:
    def __init__(self, sendTo, name):
        self.name = name
        self.inputNodes = dict() #init with low
        self.sendTo = sendTo

    def getSignal(self, pulse, fromNode):
        pulsesToSend = list()
        self.inputNodes[fromNode] = pulse
        allHigh = True
        for val in self.inputNodes.values():
            if val == 'low':
                allHigh = False
                break
        if allHigh:
            for n in self.sendTo:
                pulsesToSend.append((n, 'low', self.name))
        else:
            for n in self.sendTo:
                pulsesToSend.append((n, 'high', self.name))
        return pulsesToSend

class Broadcaster:
    def __init__(self, sendTo, name):
        self.name = name
        self.sendTo = sendTo

    def getSignal(self, pulse='low', fromNode=''):
        pulsesToSend = list()
        for n in self.sendTo:
            pulsesToSend.append((n, pulse, self.name))
        return pulsesToSend

allNodes = dict()
conjunctions = list()
for line in lines:
    schema = line.split(' -> ')
    sendTo = schema[1].split(', ')
    if schema[0] == 'broadcaster':
        allNodes['broadcaster'] = Broadcaster(sendTo, 'broadcaster')
    elif schema[0][0] == '%':
        allNodes[schema[0][1:]] = FlipFlop(sendTo, schema[0][1:])
    elif schema[0][0] == '&':
        allNodes[schema[0][1:]] = Conjunction(sendTo, schema[0][1:])
        conjunctions.append(schema[0][1:])

for name, node in allNodes.items():
    for con in conjunctions:
        if con in node.sendTo:
            allNodes[con].inputNodes[name] = 'low'

signals = Queue()

numberOfLow = 0
numberOfHigh = 0
for turn in range(0,1000):
    # print("#"*50)
    numberOfLow+=1
    init = allNodes['broadcaster'].getSignal('low', '')
    for i in init:
        signals.put(i)
    while not signals.empty():
        signal = signals.get()
        # print(signal)
        if signal[1] == 'low':
            numberOfLow += 1
        else:
            numberOfHigh += 1
        if signal[0] in allNodes:
            newSignals = allNodes[signal[0]].getSignal(signal[1], signal[2])
            for s in newSignals:
                signals.put(s)

print(numberOfHigh*numberOfLow)