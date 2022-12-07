with open('C:/Users/User/Documents/input.txt') as f:
    my_input = f.read().split('\n')
f.close()

fullpaths = {"/":[]}
backpaths = {}
dirs = {"/":0}

for line in my_input:
    if line == "$ cd /":
        last = "/"
    elif line == "$ cd ..":
        last = backpaths[last]
    elif line[0:4] == "$ cd":
        last = last + line.split(' ')[2]
        fullpaths[last] = []
    elif line[0:3] == "dir":
        dirs[last + line.split(' ')[1]] = 0
        backpaths[last + line.split(' ')[1]] = last
        fullpaths[last].append(last + line.split(' ')[1])
    elif line[0:4] != "$ ls":
        dirs[last] += int(line.split(' ')[0])
    
del last, line, f
total_sizes = {k:0 for k in dirs}
while len(fullpaths) > 0:
    dels = []
    for path, val in fullpaths.items():
        if len(val) == 0:
            total_sizes[path] += dirs[path]
            dels.append(path)
        else:
            dels2 = []
            for part in val:
                if part not in fullpaths:
                    total_sizes[path] += total_sizes[part]
                    fullpaths[path].pop(fullpaths[path].index(part))
    for atr in dels:
        fullpaths.pop(atr)
    
part1 = sum([k for k in total_sizes.values() if k <= 100000])

unused = 70000000 - total_sizes["/"] - 30000000
freed = {k:(v + unused) for k,v in total_sizes.items() if v + unused > 0}
part2 = total_sizes[[k for k,v in freed.items() if v == min(freed.values())][0]]

print(str(part1) + " " + str(part2))