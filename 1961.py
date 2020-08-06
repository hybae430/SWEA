T = int(input())

for i in range(1, T + 1):
    N = int(input())
    arr = list(list(input().split()) for _ in range(N))
    map1, map2, map3 = [], [], []

    print(f'#{i}')
    for y in range(N):
        m = []
        for x in range(N - 1, -1, -1):
            m.append(arr[x][y])
        map1.append(m)

    for x in range(N - 1, -1, -1):
        m = []
        for y in range(N - 1, -1, -1):
            m.append(arr[x][y])
        map2.append(m)

    for y in range(N - 1, -1, -1):
        m = []
        for x in range(N):
            m.append(arr[x][y])
        map3.append(m)

    for i in range(N):
        print(''.join(map1[i]), ''.join(map2[i]), ''.join(map3[i]))