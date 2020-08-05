T = int(input())

for i in range(1, T + 1):
    res = 0
    string = input()
    start = string[0]
    for j in range(1, 21):
        if start == string[j]:
            length = j
            if string[: j] == string[j : j + length]:
                res = length
                break
    print(f'#{i} {res}')