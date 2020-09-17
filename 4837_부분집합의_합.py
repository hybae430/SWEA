T = int(input())

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
s = []
for i in range(1 << len(A)):
    x = []
    for j in range(len(A)):
        if i & (1 << j):
            x.append(A[j])
    if x:
        s.append(x)

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0
    for x in s:
        if len(x) == N and sum(x) == K:
            cnt += 1
    print('#{} {}'.format(tc, cnt))