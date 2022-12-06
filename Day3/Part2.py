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

    compartments.append(set(list(line)))

    if len(compartments) < 3:
        continue
    
    compartments[0].intersection_update(compartments[1], compartments[2])

    for sect in compartments[0]:
        cIdentity = sect
    
    iSum += ord(cIdentity) - (iCapAscOff if cIdentity.isupper() else iLowAscOff)
    compartments = []

print(iSum)