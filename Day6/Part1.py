

dataStream   = []
packetMarker = []
iChar        = 0


with open('Day6/input.txt') as file:
    lines = file.readlines()

dataStream = list(lines[0])
packetMarker = [dataStream[i] for i in range(4)]

for iChar in range(4, len(dataStream)):
    if len(set(packetMarker)) == 4:
        break
    packetMarker.pop(0)
    packetMarker.append(dataStream[iChar])
print(packetMarker)
print(iChar)

