T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    min_cnt = N * M
    color = [list(input()) for _ in range(N)]
    w_cnt = 0
    for i in range(N - 2):
        for j in range(M):
            if color[i][j] != 'W':
                w_cnt += 1

        b_cnt = 0
        for j in range(i + 1, N - 1):
            for k in range(M):
                if color[j][k] != 'B':
                    b_cnt += 1

            r_cnt = 0
            for k in range(j + 1, N):
                for l in range(M):
                    if color[k][l] != 'R':
                        r_cnt += 1

            cnt = w_cnt + b_cnt + r_cnt
            if min_cnt > cnt:
                min_cnt = cnt

    print('#{} {}'.format(tc, min_cnt))





