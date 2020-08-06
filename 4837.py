arr = [i for i in range(1, 13)]
length = len(arr)
T = int(input())

subset = []

for x in range(1 << length):
    s = []
    for y in range(length):
        if x & (1 << y):
            s.append(arr[y])
    if s:
        subset.append(s)

for i in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0
    for sb in subset:
        if len(sb) == N:
            if sum(sb) == K:
                cnt += 1
    print(f'#{i} {cnt}')