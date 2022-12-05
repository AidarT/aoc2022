import re
from copy import deepcopy

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: a.split('\n'), f.read().split('\n\n')))
f.close()

stack = []
for i, num in enumerate(my_input[0][-1]):
    if num != ' ':
        stack.append([])
        for line in my_input[0]:
            if line[i].isnumeric() == False and line[i] != ' ':
                stack[-1].append(line[i])
stack2 = deepcopy(stack)
instr = [list(map(lambda a: int(a), re.findall(r'\d+', line))) for line in my_input[1]]

for line in instr:
    for i in range(0, line[0]):
        stack[line[2] - 1].insert(0, stack[line[1] - 1][0]) 
        stack[line[1] - 1].pop(0)

part1 = "".join([row[0] for row in stack])

for line in instr:
    stack2[line[2] - 1].reverse()
    stack2[line[2] - 1].extend(reversed(stack2[line[1] - 1][0:line[0]]))
    stack2[line[2] - 1].reverse()
    for i in range(0, line[0]):
        stack2[line[1] - 1].pop(0)

part2 = "".join([row[0] for row in stack2])

print(str(part1) + " " + str(part2))