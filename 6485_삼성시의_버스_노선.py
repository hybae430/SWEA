T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    stops = [0] * 5001
    for n in range(N):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            stops[i] += 1
    P = int(input())
    print('#{}'.format(tc), end=" ")
    for p in range(P):
        j = int(input())
        print(stops[j], end=" ")
    print()