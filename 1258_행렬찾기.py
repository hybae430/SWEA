T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    res = []
    for i in range(N):
        for j in range(N):
            r, c = 0, 0
            for k in range(j, N):
                if area[i][k]:
                    c += 1
                else:
                    break
            for k in range(i, N):
                if area[k][j]:
                    r += 1
                else:
                    break
            if r > 0 and c > 0:
                res.append((r, c))
                for x in range(i, i + r):
                    for y in range(j, j + c):
                        area[x][y] = 0

    res = sorted(res, key=lambda x: (x[0] * x[1], x[0]))
    print('#{} {}'.format(tc, len(res)), end=" ")
    for x, y in res:
        print(x, y, end=" ")
    print()