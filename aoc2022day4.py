import re

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = [list(map(lambda a: int(a), re.findall(r'\d+', line))) for line in f.read().split('\n')]
f.close()

part1 = 0
part2 = 0
for line in my_input:
    if ((line[2] <= line[1] and line[2] >= line[0] and line[3] <= line[1] and line[3] >= line[0]) or 
    (line[0] <= line[3] and line[0] >= line[2] and line[1] <= line[3] and line[1] >= line[2])):
        part1 += 1
    if (line[1] >= line[2] and line[2] >= line[0]) or (line[3] >= line[0] and line[0] >= line[2]):
        part2 += 1
    
print(str(part1) + " " + str(part2))