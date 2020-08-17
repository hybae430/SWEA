T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tmp, total = 0, 0
    for i in range(N):
        com = input()
        if len(com) > 1:
            a, b = map(int, com.split())
            if a == 1:
                tmp += b
            elif a == 2:
                if tmp < b:
                    tmp = 0
                else:
                    tmp -= b
        total += tmp
    print(f'#{tc} {total}')