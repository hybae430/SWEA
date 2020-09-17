T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [[0] * 10 for _ in range(10)]
    cnt = 0
    for n in range(N):
        r1, c1, r2, c2, c = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if not board[i][j]:
                    board[i][j] = c
                else:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))