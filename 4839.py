T = int(input())

def bin_search(start, end, n, cnt):
    c = int((start + end) / 2)
    if c == n:
        return cnt
    elif c > n:
        return bin_search(start, c, n, cnt + 1)
    elif c < n:
        return bin_search(c, end, n, cnt + 1)

for i in range(1, T + 1):
    P, A, B = map(int, input().split())
    result = 0
    acnt = bin_search(1, P, A, 0)
    bcnt = bin_search(1, P, B, 0)
    if acnt > bcnt:
        result = 'B'
    elif bcnt > acnt:
        result = 'A'
    print(f'#{i} {result}')