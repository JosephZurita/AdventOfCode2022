dataStream   = []
packetMarker = []
iChar        = 0
iDistinct    = 14


with open('Day6/input.txt') as file:
    lines = file.readlines()

dataStream = list(lines[0])
packetMarker = [dataStream[i] for i in range(iDistinct)]

for iChar in range(iDistinct, len(dataStream)):
    if len(set(packetMarker)) == iDistinct:
        break
    packetMarker.pop(0)
    packetMarker.append(dataStream[iChar])
print(packetMarker)
print(iChar)