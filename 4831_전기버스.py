import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))
    tmp = 0     # 현재 위치
    res = 0
    while tmp + K < N:
        if tmp + K in stops:
            tmp += K
            res += 1
        else:
            goal = 0
            for stop in stops:
                if tmp < stop < tmp + K:
                    goal = stop
            if goal:
                tmp = goal
                res += 1
            else:
                res = 0
                break
    print('#{} {}'.format(tc, res))