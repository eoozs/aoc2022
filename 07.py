# https://adventofcode.com/2022/day/7

lines = [x.strip() for x in open("input.txt", "r").readlines()]

pwd = ["_root"]
s = dict()
for line in lines[1:]:
    parts = line.split(" ")
    if parts[0] == "$":
        if parts[1] == "cd":
            if parts[2] == "..":
                pwd = pwd[:-1]
            else:
                pwd.append(parts[2])
    else:
        if parts[0] == "dir":
            continue
        else:
            for i, _ in enumerate(pwd):
                k = "/".join(pwd[:i+1])
                s[k] = s.get(k, 0) + int(parts[0])

r = 0
for k, v in s.items():
    if v < 100_000: r += v
print(r)

deletable = [(k, v) for k, v in s.items() if v >= s["_root"] - 40_000_000 ]
print(sorted(deletable, key=lambda x: x[1])[0][1])
