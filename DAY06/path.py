
with open('data.txt') as f:
    map = f.readlines()
for k in range(len(map)):
    map[k] = list(map[k].strip())

i_guard, j_guard = 0, 0
direction = "^"

for i in range(len(map)) :
    for j in range(len(map[0])) :
        if map[i][j] == direction:
            i_guard, j_guard = i, j
            break
X_count = 0
while (0 <= i_guard < len(map)) and (0 <= j_guard < len(map[0])):
    if map[i_guard][j_guard] != "X":
        map[i_guard][j_guard] = "X"
        X_count += 1
    match direction:
        case "^":
            if i_guard == 0:
                break
            if (map[i_guard - 1][j_guard] == "#"):
                direction = ">"
            else:
                i_guard -= 1
        case "v":
            if i_guard == len(map) - 1:
                break
            if (map[i_guard + 1][j_guard] == "#"):
                direction = "<"
            else:
                i_guard += 1
        case ">":
            if j_guard == len(map[0]) - 1:
                break
            if (map[i_guard][j_guard + 1] == "#"):
                direction = "v"
            else:
                j_guard += 1
        case "<":
            if j_guard == 0:
                break
            if (map[i_guard][j_guard - 1] == "#"):
                direction = "^"
            else:
                j_guard -= 1
print(X_count)