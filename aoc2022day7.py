with open('C:/Users/User/Documents/input.txt') as f:
    my_input = f.read().split('\n')
f.close()

fullpaths = {"/":[]}
paths = {}
dirs = {"/":0}
files = {}

for line in my_input:
    if line == "$ cd /":
        last = "/"
    elif line == "$ cd ..":
        last = paths[last]
    elif line[0:4] == "$ cd":       
        last = line.split(' ')[2]
        fullpaths[last] = []
    elif line[0:3] == "dir":
        dirs[line.split(' ')[1]] = 0
        paths[line.split(' ')[1]] = last
        fullpaths[last].append(line.split(' ')[1])
    elif line[0:4] != "$ ls":
        dirs[last] += int(line.split(' ')[0])
        files[line.split(' ')[1]] = int(line.split(' ')[0])

def calc_size(fullpaths, cur, dirs, total_sizes):
    if cur in fullpaths and len(fullpaths[cur]) > 0:
        for part in fullpaths[cur]:
            return dirs[cur] + calc_size(fullpaths, part, dirs, total_sizes)            
    else:
        return dirs[cur]

total_sizes = {k:0 for k in dirs}
for dir in dirs:
    total_sizes[dir] = calc_size(fullpaths, dir, dirs, total_sizes)
#total_sizes["/"] = sum(dirs.values())
        
part1 = sum([k for k in total_sizes.values() if k <= 100000])

part2 = 0

print(str(part1) + " " + str(part2))