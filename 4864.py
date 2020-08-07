T = int(input())

for i in range(1, T + 1):
    result = 0
    str1 = input()
    str2 = input()
    if str1 in str2:
        result = 1
    print(f'#{i} {result}')