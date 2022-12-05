lines  = []
moves  = []
result = 0
score  = 0 

enemyDictTL = {
    "A": 1,
    "B": 2,
    "C": 3
}

allyDictTL = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

with open('Day2/input.txt') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip('\n')
    moves = line.split()
    moves = [enemyDictTL[moves[0]], allyDictTL[moves[1]]] 
    if moves[0] % 3 == (moves[1] - 1): result = 2
    elif moves[0] == moves[1]: result = 1
    else: result = 0

    score += moves[1] + (result * 3)

print(score)
