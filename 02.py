# https://adventofcode.com/2022/day/2

rounds = [x.split(" ") for x in open("input.txt").read().split("\n") if x]

part_1 = part_2 = 0

scores = {"A": 1,  "X": 1,  "B": 2, "Y": 2, "C": 3, "Z": 3}
defeats = {1: 3, 2: 1, 3: 2}
loses = {v:k for k, v in defeats.items()}

for round in rounds:
    s1, s2 = scores[round[0]], scores[round[1]]

    if defeats[s2] == s1:
        part_1 += 6
    elif s1 == s2:
        part_1 += 3
    part_1 += s2

    if round[1] == "Y":
        part_2 += 3 + s1
    elif round[1] == "X":
        part_2 += defeats[s1]
    else:
        part_2 += 6 + loses[s1]

print(part_1)
print(part_2)
