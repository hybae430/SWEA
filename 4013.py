T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    for n in range(N):
        m, d = map(int, input().split())
        m -= 1
        ans = [(m, d)]

        # 왼쪽
        tmp = d
        for i in range(m - 1, -1, -1):
            if mag[i][2] != mag[i + 1][6]:
                tmp *= -1
                ans.append((i, tmp))
            else:
                break

        # 오른쪽
        tmp = d
        for i in range(m + 1, 4):
            if mag[i][6] != mag[i - 1][2]:
                tmp *= -1
                ans.append((i, tmp))
            else:
                break

        for m, d in ans:
            if d == 1:
                mag[m].insert(0, mag[m].pop())
            elif d == -1:
                mag[m].append(mag[m].pop(0))

    res = 0
    for i in range(4):
        res += mag[i][0] * (2 ** i)     # 1, 2, 4, 8

    print('#{} {}'.format(tc, res))