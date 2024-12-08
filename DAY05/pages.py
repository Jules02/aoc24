ordering_rules = {}

with open('data.txt') as f:
    lines = f.readlines()

sum = 0
incorrect_updates = []
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
    for j in range(len(update)):
        for k in range(0, j):
            if update[j] in ordering_rules :
                if update[k] in ordering_rules[update[j]] :
                    if b :
                        incorrect_updates.append((update, [(k, j)]))
                    else :
                        incorrect_updates[-1][1].append((k, j))
                    b = False

    if b:
        middle = len(update) // 2
        sum += int(update[middle])
    i+=1
print(sum)

new_sum = 0
for (incorrect_update, pairs) in incorrect_updates:
    for j in range(len(incorrect_update)):
        for k in range(0, j):
            if incorrect_update[j] in ordering_rules :
                if incorrect_update[k] in ordering_rules[incorrect_update[j]] :
                    incorrect_update[k], incorrect_update[j] = incorrect_update[j], incorrect_update[k]
    middle = len(incorrect_update) // 2
    new_sum += int(incorrect_update[middle])
print(new_sum)