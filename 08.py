# https://adventofcode.com/2022/day/8

m = [list(map(int, list(v))) for v in [x.strip() for x in open("input.txt", "r").readlines()]]

def is_visible(i, j):
    if i == 0 or j == 0 or i == len(m[0])-1 or j == len(m)-1:
        return True, 0

    scenic_score = 1
    visible_dirs = []
    for dir in [(-1,0), (1,0), (0,-1), (0,1)]:
        dir_score = 0
        curr = [i,j]
        while True:
            dir_score += 1
            curr[0], curr[1] = curr[0] + dir[0], curr[1] + dir[1]
            if curr[0] < 0 or curr[1] < 0:
                visible_dirs.append(True)
                dir_score -= 1
                break
            
            try:
                v = m[curr[0]][curr[1]]
                if v >= m[i][j]:
                    visible_dirs.append(False)
                    break
            except Exception as e:
                dir_score -= 1
                visible_dirs.append(True)
                break

        scenic_score *= dir_score

    return any(visible_dirs), scenic_score

best_location = (0 ,0)
best_score = -1
num_visible = 0
for i, r in enumerate(m):
    for j, c in enumerate(r):
        isv, score = is_visible(i,j)
        if isv:
            if score > best_score:
                best_score = score
                best_location = (i,j)
            num_visible += 1

print(num_visible)
print(best_score)
