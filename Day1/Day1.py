iElf   = 0
lines  = []
elfMax = []
elfHi  = 0
elfLo  = 0

with open('input.txt') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip('\n')
    if line == "":
        if elfHi < elfLo:
            elfHi = elfLo
            elfMax.clear()
            elfMax.append(iElf)
        elif elfHi == elfLo:
            elfMax.append(iElf)

        iElf += 1
        elfLo = 0

        continue

    if line.isdigit():
        elfLo += int(line)

print(elfMax)
print(elfHi)