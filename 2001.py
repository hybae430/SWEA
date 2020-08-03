T = int(input())

for idx in range(1, T + 1):
    N, M = map(int, input().split())
    flat = list(list(map(int, input().split())) for row in range(N))

    sums = []

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            total = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    total += flat[x][y]
            sums.append(total)
    
    print(f'#{idx} {max(sums)}')