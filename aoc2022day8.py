with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: list(a), f.read().split('\n')))
f.close()

scores = [[1 for x in line] for line in my_input]
part1 = 0
for i, line in enumerate(my_input):
    for j, height in enumerate(line):
        if i == 0 or j == 0 or i == len(my_input)-1 or j == len(line)-1:
            part1 += 1            
        else:
            visible = True
            score = 0
            for i1 in range(i+1, len(my_input)):
                score += 1
                if int(my_input[i1][j]) >= int(height):                    
                    visible = False
                    break
            scores[i][j] *= score
            if i1 == len(my_input)-1 and int(my_input[i1][j]) < int(height):
                visible = True
            if not visible:
                for i1 in range(i-1, -1, -1):
                    if int(my_input[i1][j]) >= int(height):
                        visible = False
                        break
                if i1 == 0 and int(my_input[i1][j]) < int(height):
                    visible = True
            score = 0
            for i1 in range(i-1, -1, -1):
                score += 1
                if int(my_input[i1][j]) >= int(height):
                    break
            scores[i][j] *= score
            if not visible:
                for j1 in range(j+1, len(line)):
                    if int(my_input[i][j1]) >= int(height):
                        visible = False
                        break
                if j1 == len(line)-1 and int(my_input[i][j1]) < int(height):
                    visible = True
            score = 0
            for j1 in range(j+1, len(line)):
                score += 1
                if int(my_input[i][j1]) >= int(height):
                    break
            scores[i][j] *= score
            if not visible:
                for j1 in range(j-1, -1, -1):
                    if int(my_input[i][j1]) >= int(height):
                        visible = False
                        break
                if j1 == 0 and int(my_input[i][j1]) < int(height):
                    visible = True
            score = 0
            for j1 in range(j-1, -1, -1):
                score += 1
                if int(my_input[i][j1]) >= int(height):
                    break
            scores[i][j] *= score
            if visible:
                part1 += 1

part2 = max([score for line in scores for score in line])

print(str(part1) + " " + str(part2))