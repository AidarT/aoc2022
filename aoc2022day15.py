import re
import operator
import math

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: list(map(lambda b: int(b), re.findall(r'-?\d+', a))), f.read().split('\n')))
f.close()

def map_create(arg):
    map_min_x = min([line[0] for line in my_input]+[line[2] for line in my_input])
    map_max_x = max([line[0] for line in my_input]+[line[2] for line in my_input])
    # map_min_y = min([line[1] for line in my_input]+[line[3] for line in my_input])
    # map_max_y = max([line[1] for line in my_input]+[line[3] for line in my_input])
    
    map_ = {}
    # map_ = {(x,y):'.' for x in range(map_min_x, map_max_x + 1) for y in range(map_min_y, map_max_y + 1)}
    # map_print = [['.' for x in range(map_min_x, map_max_x + 1)] for y in range(map_min_y, map_max_y + 1)]
    for x,y,x1,y1 in my_input:
        map_[(x,y)] = 'S'
        map_[(x1,y1)] = 'B'
        # map_print[y-map_min_y][x-map_min_x] = 'S'
        # map_print[y1-map_min_y][x1-map_min_x] = 'B'
        # if x == 8 and y == 7:
        vec = list(map(operator.sub, (x1,y1), (x,y)))
        # len_vec = math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2))
        len_vec = abs(vec[0]) + abs(vec[1])
        for x2 in range(map_min_x-abs(vec[0]), map_max_x+1+abs(vec[0])):
            # if (math.sqrt(math.pow(x2-x, 2) + math.pow(cond-y, 2))) <= len_vec:
            if abs(x2-x) + abs(cond-y) <= len_vec:
                if (x2, cond) not in map_:
                    map_[(x2, cond)] = '#'
        # marks = [coord for coord in map_ 
        #          if (math.sqrt(math.pow(coord[0]-x, 2) + math.pow(coord[1]-y, 2))) <= len_vec
        #          and coord[1] == cond]
        # for coord in marks:
        #     if map_[coord] == '.':
        #         map_[coord] = '#'
                # map_print[coord[1]-map_min_y][coord[0]-map_min_x] = '#'
    
    return map_#, map_print

cond = 10
map_ = map_create(cond)#, map_print = map_create()
# for line in map_print:
#     print(''.join(line))

part1 = len([x for x,y in map_ if y == cond and map_[(x,y)]=='#'])
part2 = 0

print(str(part1) + " " + str(part2))