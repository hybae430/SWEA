T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans, tmp = 'OFF', M
    for i in range(N):
        if not tmp % 2:
            break
        tmp //= 2
    else:
        if M != 0:
            ans = 'ON'
    print('#{} {}'.format(tc, ans))