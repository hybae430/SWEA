import sys

from itertools import combinations
import math

sys.stdin = open('sampleinput.txt')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    house, shop, cost, ans = [], [], [], []
    for y in range(N):
        tmp = list(map(int, input().split()))
        for x in range(len(tmp)):
            if tmp[x] == 1:
                house.append((y, x))
            elif tmp[x] >= 2:
                shop.append((y, x))
                cost.append(tmp[x])

    for p in combinations(shop, len(shop)):
        ret = 0
        for i in range(len(p)):
            ret += cost[shop.index(p[i])]
        for h in house:
            minval = math.inf
            for c in p:
                minval = min(abs(h[0] - c[0]) + abs(h[1] - c[1]), minval)
            ret += minval

        ans.append(ret)
    print('#{} {}'.format(tc, min(ans)))

