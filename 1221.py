nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
N = int(input())
for tc in range(N):
    tcn, n = map(str, input().split())
    num_list = list(map(str, input().split()))
    res = []
    for i in range(int(n)):
        x = nums.index(num_list[i])
        res.append(x)
    res.sort()
    print(tcn)
    for i in res:
        for j in nums:
            if i == nums.index(j):
                print(j, end=" ")
    print()
