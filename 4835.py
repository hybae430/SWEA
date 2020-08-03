T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    results = []

    for j in range(N - M + 1):
        result = 0
        for k in range(j, j + M):
            result += numbers[k]
        results.append(result)

    diff = max(results) - min(results)

    print(f'#{i} {diff}')