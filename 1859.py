T = int(input())

for i in range(1, T + 1):
    N = int(input())
    days = list(map(int, input().split()))
    start = days[-1]
    profit = 0
    for j in range(len(days) - 1, -1, -1):
        if start > days[j]:
            profit += start
            profit -= days[j]
        else:
            start = days[j]
    print(f'#{i} {profit}')