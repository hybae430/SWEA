T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    res = []
    for i in range(N - M + 1):          # 출발점 지정
        for j in range(N - M + 1):
            fly = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    fly += area[x][y]
            res.append(fly)
    print('#{} {}'.format(tc, max(res)))