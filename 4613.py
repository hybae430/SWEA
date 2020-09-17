T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 행 열
    flag = [list(input()) for _ in range(N)]
    smin = N * M

    white_cnt = 0
    for i in range(N - 2):
        for j in range(M):
            if flag[i][j] != 'W':
                white_cnt += 1

        blue_cnt = 0
        for j in range(i + 1, N - 1):
            for k in range(M):
                if flag[j][k] != 'B':
                    blue_cnt += 1

            red_cnt = 0
            for k in range(j + 1, N):
                for l in range(M):
                    if flag[k][l] != 'R':
                        red_cnt += 1

            sum = white_cnt + blue_cnt + red_cnt
            if smin > sum:
                smin = sum
    print('#{} {}'.format(tc, smin))