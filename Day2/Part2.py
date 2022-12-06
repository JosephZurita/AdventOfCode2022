lines   = []
split   = []
allyMv  = 0
result  = 0
score   = 0 

rpsDictTL = {
    "A": 1, #3
    "B": 2, #1
    "C": 3  #2
}

resDictTL = {
    "X": 0,
    "Y": 1,
    "Z": 2
}

with open('Day2/input.txt') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip('\n')
    split = line.split()
    result = resDictTL[split[1]]
    match result:
        case 0:
            allyMv = ((rpsDictTL[split[0]] + 1) % 3) + 1
        case 1:
            allyMv = rpsDictTL[split[0]]
        case 2:
            allyMv = (rpsDictTL[split[0]] % 3) + 1 

    score += allyMv + (result * 3)

print(score)
