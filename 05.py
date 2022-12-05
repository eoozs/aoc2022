# https://adventofcode.com/2022/day/5

def read_deck():
    lines = open("input.txt").read().split("\n")

    empty_line_idx = lines.index("") 
    values = lines[:empty_line_idx-1]
    numbers = [int(n) for n in lines[empty_line_idx-1].split(" ") if n]
    instructions = [i for i in lines[empty_line_idx+1:] if i]

    deck = {}
    for value in values:
        for i, v in enumerate(range(0, numbers[-1]*4, 4)):
            if numbers[i] not in deck:
                deck[numbers[i]] = []
            val = value[v:v+3].strip().replace("[", "").replace("]", "")
            if val:
                deck[numbers[i]].append(val)
    return deck, instructions, numbers

deck1, instructions, numbers = read_deck()
deck2, _, _ = read_deck()
for ins in instructions:
    parts = [int(x) for x in ins.split(" ") if x.isdigit()]
    insert = [deck1[parts[1]].pop(0) for i in range(parts[0])][::-1]
    deck1[parts[2]] = insert + deck1[parts[2]]
    insert = [deck2[parts[1]].pop(0) for i in range(parts[0])]
    deck2[parts[2]] = insert + deck2[parts[2]]

print("".join([deck1[num][0] for num in numbers]))
print("".join([deck2[num][0] for num in numbers]))
