import string

with open('C:/Users/User/Documents/input.txt') as f:
    my_input2 = f.read().split('\n')    
f.close()
my_input = [[line[:int(len(line)/2)], line[int(len(line)/2):]] for line in my_input2]

my_input = [[list(set(line[0])), list(set(line[1]))] for line in my_input]
priorities = [let for line in my_input for let in line[0] if let in line[1]]
alphabet = {k:(v + 1) for v, k in enumerate(string.ascii_letters)}

part1 = sum([alphabet[let] for let in priorities])

priorities = []
for i in range(0, len(my_input2), 3):
    overlap = [let for let in my_input2[i] if let in my_input2[i+1] if let in my_input2[i+2]][0]
    priorities.append(alphabet[overlap])

part2 = sum(priorities)

print(str(part1) + " " + str(part2))