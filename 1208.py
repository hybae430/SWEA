for i in range(1, 11):
    dump = int(input())
    datas = list(map(int, input().split()))

    while max(datas) - min(datas) > 1 and dump > 0:
        big = datas.index(max(datas))
        small = datas.index(min(datas))

        datas[big] -= 1
        datas[small] += 1
        dump -= 1

    diff = max(datas) - min(datas)

    print(f'#{i} {diff}')