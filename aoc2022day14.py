import operator

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: list(map(lambda b:list(map(lambda c:int(c), b.split(','))), 
                                           a.split(' -> '))), f.read().split('\n')))
f.close()

def map_create(arg, part2 = False):
    map_min_x = min([x for line in my_input for x,y in line])
    map_max_x = max([x for line in my_input for x,y in line])
    map_max_y = max([y for line in my_input for x,y in line]) + arg
    
    map_ = {(x,y):'.' for x in range(map_min_x, map_max_x + 1) for y in range(0, map_max_y + 1)}
    if part2:
        for x in range(map_min_x, map_max_x + 1):
            map_[(x, map_max_y)] = '#'
    return map_, map_min_x

def fill_map():
    for line in my_input:
        for i in range(0, len(line)-1):
            start = tuple(line[i])
            end = tuple(line[i+1])
            dif = tuple([int(n/abs(n)) if n != 0 else 0 for n in map(operator.sub, end, start)])
            map_[end] = '#'
            while (start != end):
                map_[start] = '#'
                start = tuple(map(operator.add, start, dif))        

moves = [(0,1), (-1,1), (1,1)]

def nextMoveIs(cur):
    for move in moves:
        next_ = tuple(map(operator.add, cur, move))
        if next_ in map_:
            if map_[next_] != "#" and map_[next_] != "o":
                return nextMoveIs(next_)
        else:
            return -1
    return cur

def print_map():
    x_vals = [x for x,y in map_]
    map_min_x = min(x_vals)
    map_max_x = max(x_vals)
    map_max_y = max([y for x,y in map_])
    map_print = [['.' for x in range(map_min_x, map_max_x + 1)] for y in range(0, map_max_y + 1)]
    for x,y in map_:
        map_print[y][x - map_min_x] = map_[x,y]
    for line in map_print:
        print(''.join(line))

map_, map_min_x = map_create(0)
fill_map()
part1 = 0

while True:
    sand = (500,-1)
    next_ = nextMoveIs(sand)
    if next_ == -1:
        break
    else:
        map_[next_] = "o"
        part1 += 1

print_map()

def fill_row(next_):
    x = next_[0]
    map_max_y = max([y for x,y in map_])
    for y in range(0, map_max_y + 1):
        map_[(x,y)] = "."
    map_[(x,map_max_y)] = "#"
    

def part2NextMoveIs(cur):
    for move in moves:
        next_ = tuple(map(operator.add, cur, move))
        if next_ not in map_:
            fill_row(next_)
        if map_[next_] != "#" and map_[next_] != "o":
            return part2NextMoveIs(next_)
    return cur

map_, map_min_x = map_create(2, True)
fill_map()
part2 = 0

while True:
    sand = (500,-1)
    next_ = part2NextMoveIs(sand)
    if next_ == (500,0):
        map_[next_] = "o"
        part2 += 1
        break
    else:
        map_[next_] = "o"
        part2 += 1

print_map()

print(str(part1) + " " + str(part2))