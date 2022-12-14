import operator

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: list(map(lambda b:list(map(lambda c:int(c), b.split(','))), 
                                           a.split(' -> '))), f.read().split('\n')))
f.close()

map_min_x = min([x for line in my_input for x,y in line])
map_max_x = max([x for line in my_input for x,y in line])
map_max_y = max([y for line in my_input for x,y in line])

map_ = {(x,y):'.' for x in range(map_min_x, map_max_x + 1) for y in range(0, map_max_y + 1)}
map_print = [['.' for x in range(map_min_x, map_max_x + 1)] for y in range(0, map_max_y + 1)]
del map_max_x, map_max_y

for line in my_input:
    for i in range(0, len(line)-1):
        start = tuple(line[i])
        end = tuple(line[i+1])
        dif = tuple([int(n/abs(n)) if n != 0 else 0 for n in map(operator.sub, end, start)])
        map_[end] = '#'
        while (start != end):
            map_[start] = '#'
            start = tuple(map(operator.add, start, dif))
            
del start, end, dif
#sand = (500,0)
moves = [(0,1), (-1,1), (1,1)]
for x,y in map_:
    map_print[y][x-map_min_x] = map_[x,y]

def nextMoveIs(cur):
    for move in moves:
        next_ = tuple(map(operator.add, cur, move))
        if next_ in map_:
            if map_[next_] != "#" and map_[next_] != "o":
                return nextMoveIs(next_)
            else:
                return cur
        else:
            return -1

while True:
    sand = (500,-1)
    next_ = nextMoveIs(sand)
    if next_ == -1:
        break
    else:
        map_[next_] = "o"
        map_print[next_[1]][next_[0]-map_min_x] = map_[next_]
        
for x,y in map_:
    map_print[y][x-map_min_x] = map_[x,y]
for line in map_print:
    print(''.join(line))

part1 = 0
part2 = 0

print(str(part1) + " " + str(part2))