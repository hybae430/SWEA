T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    for m in money:
        print(N // m, end = " ")
        N %= m
    print()