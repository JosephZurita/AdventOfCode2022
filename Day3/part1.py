lines        = []
iHalfLen     = 0
iCapAscOff   = 38
iLowAscOff   = 96
iSum         = 0
cIdentity    = ""
compartments = []

with open('Day3/input.txt') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip('\n')

    iHalfLen = len(line) / 2

    if (iHalfLen % 1) != 0:
        continue
    iHalfLen = int(iHalfLen)

    compartments = [set(list(line[:iHalfLen])), set(list(line[iHalfLen:]))]
    compartments[0].intersection_update(compartments[1])

    if len(compartments[0]) != 1:
        continue

    for sect in compartments[0]:
        cIdentity = sect
    
    iSum += ord(cIdentity) - (iCapAscOff if cIdentity.isupper() else iLowAscOff)

print(iSum)