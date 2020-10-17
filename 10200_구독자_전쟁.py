T = int(input())
for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    n_min = 0
    if A + B >= N:
        n_min = (A + B) - N
    print('#{} {} {}'.format(tc, min(A, B), n_min))