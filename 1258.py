T = int(input())

for i in range(1, T + 1):
    N = int(input())
    sq = list(list(map(int, input().split())) for row in range(N))
    dic = {}

    for y in range(N):
        cnt = 0
        for x in range(N):
            if sq[y][x]:
                cnt += 1
            elif sq[y][x] == 0 and cnt != 0:
                dic[cnt] = dic.get(cnt, 0) + 1
                cnt = 0
        if cnt > 0:
            dic[cnt] = dic.get(cnt, 0) + 1
    matrix = []
    for c, r in dic.items():
        matrix.append((c * r, r, c))
    matrix.sort()
    print(f'#{i} {len(matrix)}', end = ' ')
    for i in range(len(matrix)):
        print(matrix[i][1], matrix[i][2], end = ' ')
    print()