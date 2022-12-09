import operator

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: a.split(" "), f.read().split('\n')))
f.close()

moves = {"U":(0,1), "D":(0,-1), "L":(-1,0), "R":(1,0)}
tail_moves = [(0,0), (0,1), (0,-1), (-1,0), (1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

mapT1 = {(0,0):1}
mapT9 = {(0,0):1}

def calc_posH(pos, dir):
    new_pos = tuple(map(operator.add, pos, moves[dir]))
    return new_pos

def calc_posT(pos, posH):
    dif = tuple(map(operator.sub, posH, pos))
    if dif not in tail_moves:
        moveT = [tuple(map(operator.add, dif, moveH)) for moveH in tail_moves 
                 if tuple(map(operator.add, dif, moveH)) in tail_moves]
        return tuple(map(operator.add, pos, moveT[0]))
    else:
        return pos

posH = (0,0)
posT1,posT2,posT3,posT4,posT5,posT6,posT7,posT8,posT9 = (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)
for move in my_input:
    dir, count = move
    for i in range(0, int(count)):
        posH = calc_posH(posH, dir)
        posT1 = calc_posT(posT1, posH)
        mapT1[posT1] = 1
        posT2 = calc_posT(posT2, posT1)
        posT3 = calc_posT(posT3, posT2)
        posT4 = calc_posT(posT4, posT3)
        posT5 = calc_posT(posT5, posT4)
        posT6 = calc_posT(posT6, posT5)
        posT7 = calc_posT(posT7, posT6)
        posT8 = calc_posT(posT8, posT7)
        posT9 = calc_posT(posT9, posT8)
        mapT9[posT9] = 1

part1 = len(mapT1)

part2 = len(mapT9)

print(str(part1) + " " + str(part2))