for tc in range(1, 11):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for x in range(100):
        check = 0
        for y in range(100):
            if area[y][x] == 0:
                continue
            elif not check and area[y][x] == 2:
                continue
            elif check and area[y][x] == 2:
                cnt += 1
                check = 0
            elif area[y][x] == 1:
                check = 1
    print('#{} {}'.format(tc, cnt))