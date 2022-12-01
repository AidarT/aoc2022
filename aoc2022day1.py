with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: sum(list(map(lambda b: int(b), a.split('\n')))), f.read().split('\n\n')))
f.close()

part1 = max(my_input)

my_input.sort(reverse=True)

part2 = sum(my_input[0:3])

print(str(part1) + " " + str(part2))
