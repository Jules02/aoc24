with open('data.txt') as f:
    lines = f.readlines()

leftList, rightList = [], []

for line in lines:
    leftString, rightString = '', ''
    i = 0
    while line[i] != ' ':
        leftString += line[i]
        i += 1
    i += 3
    while i < len(line):
        if line[i] == '\n':
            break
        rightString += line[i]
        i += 1
    leftList.append(int(leftString))
    rightList.append(int(rightString))

sortedLeftList = sorted(leftList)
sortedRightList = sorted(rightList)

distances = []

for i in range(len(lines)) :
    left = sortedLeftList[i]
    right = sortedRightList[i]
    distances.append(abs(left - right))

# ANSWER FOR PART 1
print(sum(distances))



occurences = {}
for i in range(len(leftList)) :
    if leftList[i] not in occurences:
        s = 0
        for j in range(len(rightList)) :
            s += 1 if (rightList[j] == leftList[i]) else 0
        occurences[leftList[i]] = s

similarity = 0
for i in range(len(leftList)) :
    similarity += leftList[i] * occurences[leftList[i]]

# ANSWER FOR PART 2
print(similarity)