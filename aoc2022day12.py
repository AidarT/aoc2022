import operator

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: list(a), f.read().split('\n')))
f.close()

map_ = {(i,j):v for j, line in enumerate(my_input) for i, v in enumerate(line)}
moves = [(0,1), (0,-1), (-1,0), (1,0)]

start = list(map_.keys())[[list(map_.values()).index(k) for k in map_.values() if k == "S"][0]]
map_[start] = "a"
end = list(map_.keys())[[list(map_.values()).index(k) for k in map_.values() if k == "E"][0]]
map_[end] = "z"

el_a = {k:v for k,v in map_.items() if v == "a"}
lengths_a = {k:float("inf") for k in el_a}
        
for st in el_a:
    visited = {k:False for k in map_}
    lengths = {k:float("inf") for k in map_}
    lengths[st] = 0
    cur = st
            
    while(cur != -1):
        for move in moves:
            next_ = tuple(map(operator.add, cur, move))
            if next_ in map_ and (ord(map_[next_]) - ord(map_[cur])) <= 1:
                if (lengths[cur] + 1 < lengths[next_]):
                    lengths[next_] = 1 + lengths[cur]
        visited[cur] = True
        cur = -1;
        min_len = float("inf");
        for i in map_:
          if (not visited[i] and (lengths[i] < min_len)):
            cur = i
            min_len = lengths[i];
            
    lengths_a[st] = lengths[end]

part1 = lengths_a[start]
part2 = min(lengths_a.values())

print(str(part1) + " " + str(part2))