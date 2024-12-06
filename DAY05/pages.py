ordering_rules = {}

with open('data.txt') as f:
    lines = f.readlines()

sum = 0
i = 0
while lines[i] != "\n" :
    before, after = lines[i].split("|")[0], lines[i].split("|")[1][:-1]
    if before not in ordering_rules:
        ordering_rules[before] = [after]
    else:
        ordering_rules[before].append(after)
    i+=1
i+=1
while i < len(lines):
    b = True
    update = lines[i].split(",")
    update[-1] = update[-1][:-1]
    for j in range(len(update) - 1):
        for k in range(j+1, len(update)):
            b = (update[k] in ordering_rules[update[j]]) and b
    if b:
        middle = len(update) // 2
        sum += int(update[middle])
    i+=1
print(sum)
