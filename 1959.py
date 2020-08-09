T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = []
    if N > M:
        l, long, s, short = N, A, M, B
    else:
        l, long, s, short = M, B, N, A
    for i in range(l - s + 1):
        total = 0
        idx = 0
        for j in range(i, i + s):
            total += long[j] * short[idx]
            idx += 1
        res.append(total)
    print(f'#{tc} {max(res)}')