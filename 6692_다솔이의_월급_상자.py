T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    avg = 0
    for n in range(N):
        p, x = map(float, input().split())
        avg += p * x
    print('#{} {}'.format(tc, avg))