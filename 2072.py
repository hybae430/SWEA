T = int(input())

for i in range(1, T + 1):
    total = 0
    numlist = map(int, input().split())
    for num in numlist:
        if num % 2:
            total += num
    print(f'#{i} {total}')