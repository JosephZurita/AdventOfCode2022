lines     = []
line      = ""
hori      = []
jaggStack = []
iPtr      = 0
iMag      = 0
iFrom     = 0
iTo       = 0
cOrder    = ""

with open('Day5/input.txt') as file:
    lines = file.readlines()

line = lines[iPtr].strip('\n')
while line != "":
    line = [block for ind, block in enumerate(line) if ((ind - 1) % 4) == 0 ]
    hori.append(line)
    iPtr += 1
    line = lines[iPtr].strip('\n')#

#Don't need last line as excess data
hori.pop()
#All lines should be same length
jaggStack = [[line[ind] for line in reversed(hori) if line[ind] != " "] for ind in range(len(hori[0]))]

for iPtr in range(iPtr + 1, len(lines)):
    line = (lines[iPtr].strip('\n')).split()
    iMag, iFrom, iTo = int(line[1]), int(line[3]), int(line[5])

    for iMag in range(iMag):
        jaggStack[iTo - 1].append(jaggStack[iFrom - 1].pop())

print("".join([stack[len(stack) - 1] for stack in jaggStack]))