T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    res = []
    print(f'#{tc}')
    for i in range(N):
        alp, num = map(str, input().split())
        res.extend([alp] * int(num))
    for idx, x in enumerate(res):
        if idx != 0 and idx % 10 == 0:
            print()
        if idx % 10 < 10:
            print(x, end = "")
    print()