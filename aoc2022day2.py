with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: a.split(' '), f.read().split('\n')))
f.close()

shape = {'X':1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C':3}

part1 = 0
for line in my_input:
    part1 += (shape[line[1]] 
    + (6 if ((shape[line[1]] - shape[line[0]] == -2 or shape[line[1]] > shape[line[0]])
             and shape[line[1]] - shape[line[0]] != 2) else 
       (3 if shape[line[1]] == shape[line[0]] else 0)))

shape = {'X':0, 'Y':3, 'Z':6, 'A':1, 'B':2, 'C':3}

part2 = 0
for line in my_input:
    part2 += (shape[line[1]] 
    + ((3 if shape[line[0]] == 2 else (2 if shape[line[0]] == 1 else 1)) if shape[line[1]] == 6 else 0) 
    + ((3 if shape[line[0]] == 3 else (2 if shape[line[0]] == 2 else 1)) if shape[line[1]] == 3 else 0) 
    + ((3 if shape[line[0]] == 1 else (2 if shape[line[0]] == 3 else 1)) if shape[line[1]] == 0 else 0))
    
print(str(part1) + " " + str(part2))