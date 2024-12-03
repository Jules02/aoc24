digits="0123456789"

with open('data.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    i = 0
    while i < len(line) - 4:
        if line[i:i+4] == "mul(" :
            X_asStr = ""
            i = i+4
            while (i < len(line) - 2 and line[i] in digits):
                X_asStr+=line[i]
                i+=1
            if (line[i] == ',') :
                X = int(X_asStr)
                Y_asStr = ""
                i += 1
                while (i < len(line) - 1 and line[i] in digits):
                    Y_asStr+=line[i]
                    i+=1
                if line[i] == ')':
                    Y = int(Y_asStr)
                    prod = X * Y
                    sum += prod
        i+=1

print(sum)

