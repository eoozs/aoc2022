# https://adventofcode.com/2022/day/4

ranges = [list(map(int, x.replace(",","-").split("-"))) for x in open("input.txt").read().split("\n") if x]

s1 = s2 = 0
for r in ranges:
    s1 = s1 + 1 if (r[0] >= r[2] and r[1] <= r[3]) or (r[2] >= r[0] and r[3] <= r[1]) else s1
    s2 = s2 + 1 if set(range(r[0], r[1]+1)).intersection(set(range(r[2], r[3]+1))) else s2

print(s1)
print(s2)
