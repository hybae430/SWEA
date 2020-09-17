import sys
sys.stdin = open('input.txt', 'r')

for n in range(10):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr2 = list(map(list, zip(*arr)))
    res = []
    d1, d2 = 0, 0   # 대각선 합
    for i in range(100):
        res.append(sum(arr[i]))
        res.append(sum(arr2[i]))
        d1 += arr[i][i]
        d2 += arr[i][99 - i]
    res.append(d1)
    res.append(d2)
    print('#{} {}'.format(tc, max(res)))