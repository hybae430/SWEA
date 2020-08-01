abc = input()
result = []

for x in abc:
    result.append(ord(x) - 64)

for i in range(len(result)):
    print(result[i], end = " ")