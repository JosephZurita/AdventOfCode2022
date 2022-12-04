iElf      = 0
iElfLimit = 3
lines     = []
topElfs   = []
elfHi     = 0
elfCal    = 0

def topElfCalc(cal):
    i = 0
    iElfLen = len(topElfs)
    iElfPos = -1

    if iElfLen == 0:
        topElfs.append(cal)
        return

    for i in range(iElfLen - 1, -1, -1):
        if topElfs[i] > cal:
            break
        iElfPos = i

    if iElfLen < iElfLimit:
        if iElfPos == -1: topElfs.append(cal)
        else            : topElfs.insert(iElfPos, cal)
        return
    
    if iElfPos == -1:
        return
    topElfs.insert(iElfPos, cal)
    topElfs.pop(iElfLen)

with open('input.txt') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip('\n')
    if line == "":
        topElfCalc(elfCal)
        elfCal = 0
        continue

    if line.isdigit():
        elfCal += int(line)

print(topElfs)
print(sum(topElfs))


    
    
    

