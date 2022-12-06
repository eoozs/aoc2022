# https://adventofcode.com/2022/day/6

v = open("input.txt", "r").read().strip()

for length in (4, 14):
    for j in range(length, len(v)):
        if len(set(v[j-length:j])) == length:
            print(j)
            break
