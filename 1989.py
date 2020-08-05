T = int(input())

for i in range(1, T + 1):
    string = input()
    ispal = True
    for j in range(len(string) // 2):
        if string[j] != string[- j - 1]:
            ispal = False
            break
    print(f'#{i} {int(ispal)}')