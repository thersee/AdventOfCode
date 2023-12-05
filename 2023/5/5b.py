from collections import defaultdict

with open('5/inputTest.txt') as f:
    lines = f.read().splitlines()

seeds = lines[0].split(':')[1].strip().split(' ')

maps = defaultdict(dict)


locations = list()

for s in range(0, len(seeds), 2):
    ran = (int(seeds[s]), int(seeds[s])+int(seeds[s+1])-1)
    ranges = [ran]
    transformedRanges = []
    for line in lines[2:]:
        if line != '' and not line[0].isdigit():
            ranges.extend(transformedRanges)
            print("#"*50)
            print('ranges', ranges)
            transformedRanges = []
        elif line != '':
            # print("#"*50)
            # print(line)
            numbers = line.split(' ')
            dest = int(numbers[0])
            source = int(numbers[1])
            ran = int(numbers[2])
            toAdd = dest - source
            nextRanges = []
            for r in ranges:
                start = r[0]
                end = r[1]
                # print(r)
                if start >= source and end < source+ran:
                    # print('inne')
                    #helt inne i intervallet
                    transformedRanges.append((start+toAdd, end+toAdd)) #add transformation
                elif start < source and end >= source+ran:  
                    # print('ute')
                    #omsluter helt intervallet
                    nextRanges.append((start, source -1))
                    nextRanges.append((source + ran, end))
                    transformedRanges.append((source+toAdd, source+ran+toAdd)) #add transformation
                elif start >= source and start < source + ran and end >= source+ran:
                    # print('början')
                    #början är med men inte slutet
                    transformedRanges.append((start+toAdd, source+ran+toAdd)) #add transformation
                    nextRanges.append((source + ran, end))
                elif start < source and end >= source and end < source+ran:
                    # print('slutet')
                    #slutet är med men inte början
                    transformedRanges.append((source+toAdd, end+toAdd)) #add transformation
                    nextRanges.append((start, source-1))
                else:
                    # print('inget')
                    nextRanges.append((start, end))
            ranges = nextRanges
            # print('transformedRanges', transformedRanges)

    locations.extend(ranges)            

locations.sort()
print(locations[0][0])