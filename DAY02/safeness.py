with open('data.txt') as f:
    lines = f.readlines()

levels = []
for line in lines:
    level = []
    i = 0
    n_asStr = ""
    while i < len(line) :
        if line[i] == '\n':
            break
        if line[i] == ' ':
            level.append(int(n_asStr))
            n_asStr = ""
        else :
            n_asStr += line[i]
        i+=1
    level.append(int(n_asStr))
    levels.append(level)

def signe(x) :
    return 1 if (x > 0) else 0 if (x==0) else -1

### PART 1

def isSafe(level) :
    m = len(level)
    way = signe(level[1] - level[0])
    for i in range(m-1):
        step = level[i+1] - level[i]
        if not(signe(step) == way and (1 <= abs(step) <= 3)) :
            return False
    return True

safe = 0
for level in levels:
    if isSafe(level) :
        safe += 1

# ANSWER FOR PART 1
print(safe)



### PART 2

def isSafeStep(step, way) :
    return (signe(step) == way and (1 <= abs(step) <= 3))

def isAlmostSafe(level) :
    m = len(level)

    exception = 0

    i = 1

    firstStep = level[1] - level[0]
    way = signe(firstStep)

    secondStep = level[2] - level[1]
    thirdStep = level[3] - level[2]
    jumpStep = level[2] - level[0]

    if not(1 <= abs(firstStep) <= 3) :
        return isSafe(level[1:])
    if way != signe(secondStep) :
        # if way switches between the first two steps, either ignore the first or the second element
        if (signe(jumpStep) == signe(thirdStep) and (1 <= abs(jumpStep) <= 3)):
            # ignore the second element
            exception = 1
            way = signe(jumpStep)
            i = 2
        else :
            # ignore the first element
            return isSafe(level[1:])

    while i < m - 1:
        step = level[i+1] - level[i]

        if not isSafeStep(step, way) :
            if exception == 0 :
                if i + 1 == m - 1 :    # only the final step is problematic
                    return True
                # elsewise, let's ignore level[i + 1]
                newStep = level[i + 2] - level[i]
                if isSafeStep(newStep, way):
                    exception = 1
                    i += 2
                    continue
            return False
        i += 1
    return True


def stupid_isAlmostSafe(level) :
    if isSafe(level) :
        return True
    b = False
    for i in range(len(level)):
        b = b or isSafe(level[:i] + level[i+1:])
    return b


almostSafe = 0
for level in levels:
    if isAlmostSafe(level) :
        almostSafe += 1

 # ANSWER FOR PART 2
print(isAlmostSafe([70, 72, 69, 68, 65, 63, 60]))
print(almostSafe)