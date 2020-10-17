T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lines = []
    cnt = 0
    for n in range(N):
        A, B = map(int, input().split())
        for line in lines:
            if (A > line[0] and B > line[1]) or (A < line[0] and B < line[1]):
                continue
            cnt += 1
        lines.append((A, B))
    print('#{} {}'.format(tc, cnt))