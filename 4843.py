T = int(input())

for i in range(1, T + 1):
    N = int(input())
    numlist = list(map(int, input().split()))
    res = []
    numlist.sort(reverse = True)
    for j in range(5):
        res.append(numlist[j])
        res.append(numlist[N - j - 1])
    print(f'#{i}', end = " ")
    for j in range(len(res)):
        print(res[j], end = " ")
