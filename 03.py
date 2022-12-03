# https://adventofcode.com/2022/day/3

import string

rows = [row for row in open("input.txt", "r").read().split("\n") if row]
scores = string.ascii_lowercase + string.ascii_uppercase

print(sum([sum([scores.index(c) + 1 for c in set(row[:len(row)//2]).intersection(set(row[len(row)//2:]))]) for row in rows]))

s = 0
for i in range(0, len(rows), 3):
    s += sum([scores.index(c) + 1 for c in set(rows[i]).intersection(rows[i+1]).intersection(rows[i+2])])
print(s)
