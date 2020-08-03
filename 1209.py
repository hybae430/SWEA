for idx in range(10):
    T = int(input())
    numlist = list(list(map(int, input().split())) for row in range(100))
    sums = []
    
    for i in range(100):
        sums.append(sum(numlist[i]))
    
    for i in range(100):
        total = 0
        for j in range(100):
            total += numlist[j][i]
        sums.append(total)
    
    zig = 0
    zag = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                zig += numlist[i][j]
            if i + j == 100:
                zag += numlist[i][j]

    sums.append(zig)
    sums.append(zag)
    
    print(f'#{T} {max(sums)}')