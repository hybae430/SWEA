for tc in range(1, 11):
    N = int(input())
    bd = list(map(int, input().split()))
    res = 0
    for i in range(2, N - 2):
        b = [bd[i - 2], bd[i - 1], bd[i + 1], bd[i + 2]]
        idx = max(b)
        if bd[i] > idx:
            res += bd[i] - idx
    print('#{} {}'.format(tc, res))