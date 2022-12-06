with open('C:/Users/User/Documents/input.txt') as f:
    my_input = f.read()
f.close()

part1 = 0
for i in range(0, len(my_input)-4):
    marker = my_input[i:i+4]
    if len(list(set(marker))) == 4:
        part1 = i + 4
        break

part2 = 0
for i in range(0, len(my_input)-14):
    marker = my_input[i:i+14]
    if len(list(set(marker))) == 14:
        part2 = i + 14
        break

print(str(part1) + " " + str(part2))