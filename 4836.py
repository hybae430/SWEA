T = int(input())
purple = {1, 2}

for i in range(1, T + 1):
    pal = [[0] * 10 for _ in range(10)]
    N = int(input())
    for j in range(N):
        x1, y1, x2, y2, col = map(int, input().split())
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if pal[x][y]:
                    pal[x][y].add(col)
                else:
                    pal[x][y] = {col}
    cnt = 0
    for j in range(10):
        cnt += pal[j].count(purple)
    print(f'#{i} {cnt}')