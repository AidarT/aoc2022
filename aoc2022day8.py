with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: list(a), f.read().split('\n')))
f.close()

def isVisible(my_input, height, i, j, bord1, bord2, step, cond, isColumn):
    if isColumn:
        for i1 in range(bord1, bord2, step):
            if int(my_input[i1][j]) >= int(height):
                return False
        if i1 == cond and int(my_input[i1][j]) < int(height):
            return True
    else:
        for j1 in range(bord1, bord2, step):
            if int(my_input[i][j1]) >= int(height):
                return False
        if j1 == cond and int(my_input[i][j1]) < int(height):
            return True
        
def calcScore(my_input, height, i, j, bord1, bord2, step, isColumn):
    score = 0
    if isColumn:        
        for i1 in range(bord1, bord2, step):
            score += 1
            if int(my_input[i1][j]) >= int(height):
                break
    else:
        for j1 in range(bord1, bord2, step):
            score += 1
            if int(my_input[i][j1]) >= int(height):
                break
    return score

scores = [[1 for x in line] for line in my_input]
part1 = 0
for i, line in enumerate(my_input):
    for j, height in enumerate(line):
        if i == 0 or j == 0 or i == len(my_input)-1 or j == len(line)-1:
            part1 += 1            
        else:
            visible = isVisible(my_input, height, i, j, i+1, len(my_input), 1, len(my_input)-1, True)            
            scores[i][j] *= calcScore(my_input, height, i, j, i+1, len(my_input), 1, True)
            if not visible:
                visible = isVisible(my_input, height, i, j, i-1, -1, -1, 0, True)
            scores[i][j] *= calcScore(my_input, height, i, j, i-1, -1, -1, True)
            if not visible:
                visible = isVisible(my_input, height, i, j, j+1, len(line), 1, len(line)-1, False)
            scores[i][j] *= calcScore(my_input, height, i, j, j+1, len(line), 1, False)
            if not visible:
                visible = isVisible(my_input, height, i, j, j-1, -1, -1, 0, False)
            scores[i][j] *= calcScore(my_input, height, i, j, j-1, -1, -1, False)
            if visible:
                part1 += 1

part2 = max([score for line in scores for score in line])

print(str(part1) + " " + str(part2))