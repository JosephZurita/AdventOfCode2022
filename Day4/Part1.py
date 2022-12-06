lines    = []
pairList = []
iSum     = 0

with open('Day4/input.txt') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip('\n')
    pairList = [p.split("-") for p in line.split(",")]
    pairList = [[int(item[0]), int(item[1])] for item in pairList]
    if (pairList[0][0] >= pairList[1][0] and pairList[0][1] <= pairList[1][1]) or (pairList[1][0] >= pairList[0][0] and pairList[1][1] <= pairList[0][1]):
        iSum += 1

    
print(iSum)