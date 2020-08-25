T = int(input())
for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    M = min(A, B)
    if A + B <= N:
        m = 0
    else:
        m = A + B - N
    print(f'#{tc} {M} {m}')
#
result =[]
T = int(input())
for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    M = min(A, B)
    if A + B <= N:
        m = 0
    else:
        m = A + B - N
    result.append(f'#{tc} {M} {m}')
for i in range(len(result)):
    print(result[i])