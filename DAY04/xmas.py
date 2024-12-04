with open('data.txt') as f:
    lines = f.readlines()

sum = 0

neighbors = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) != (0, 0)]
mas = "XMAS"
for i in range(len(lines)) :
    for j in range(len(lines[i])):
        if lines[i][j] == "X" :
            for (x, y) in neighbors :
                k = 1
                i_n, j_n = i + x, j + y
                while (k < 4 and (0 <= i_n < len(lines) and 0 <= j_n < len(lines[i_n])) and lines[i_n][j_n] == mas[k]):
                    i_n, j_n = i_n + x, j_n + y
                    k += 1
                if (k == 4) :
                    sum += 1
print(sum)

Xneighbors = [["M", "M", "S", "S"], ["M", "S", "M", "S"], ["S", "S", "M", "M"], ["S", "M", "S", "M"]]
sum2 = 0
for i in range(1, len(lines) - 1) :
    for j in range(1, len(lines[i]) - 1):
        if lines[i][j] == "A":
            if [lines[i-1][j-1], lines[i+1][j-1], lines[i-1][j+1], lines[i+1][j+1]] in Xneighbors:
                sum2 += 1
print(sum2)


