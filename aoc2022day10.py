with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: a.split(" "), f.read().split('\n')))
f.close()

x = 1
cycle = 0
part1 = 0
border = 20
screen = [['.' for i in range(0,40)] for j in range(0,6)]
CRT = 0
CRT_line = 0
CRT_border = 39
for line in my_input:
    if cycle > CRT_border:
        CRT_line += 1
        CRT_border += 40
        CRT = 0
    if CRT == x-1:
        screen[CRT_line][x-1] = '#'
    if CRT == x:
        screen[CRT_line][x] = '#'
    if CRT == x+1:
        screen[CRT_line][x+1] = '#'    
    CRT += 1
    cycle += 1
    if cycle == border:
        part1 += cycle * x
        border += 40
    if len(line) > 1:
        if cycle > CRT_border:
            CRT_line += 1
            CRT_border += 40
            CRT = 0
        if CRT == x-1:
            screen[CRT_line][x-1] = '#'
        if CRT == x:
            screen[CRT_line][x] = '#'
        if CRT == x+1:
            screen[CRT_line][x+1] = '#'    
        CRT += 1
        cycle += 1
        if cycle == border:
            part1 += cycle * x
            border += 40
        x += int(line[1])        

for line in screen:
    print(''.join(line))
part2 = 0

print(str(part1) + " " + str(part2))