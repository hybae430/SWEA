T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    res = []
    for i in range(N - M + 1):
        x = 0
        for j in range(M):
            x += nums[i + j]
        res.append(x)
    print('#{} {}'.format(tc, max(res) - min(res)))