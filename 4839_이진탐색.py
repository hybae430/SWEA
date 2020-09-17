T = int(input())

def bin_search(l, r, ans):
    x = int((l + r) / 2)
    if x == ans:
        return 1
    elif x < ans:
        return bin_search(x, r, ans) + 1
    else:
        return bin_search(l, x, ans) + 1

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    if bin_search(1, P, A) > bin_search(1, P, B):
        res = 'B'
    elif bin_search(1, P, A) < bin_search(1, P, B):
        res = 'A'
    else:
        res = 0
    print('#{} {}'.format(tc, res))