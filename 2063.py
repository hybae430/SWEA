N = int(input())

numlist = list(map(int, input().split()))
numlist.sort()
middle = len(numlist) // 2
print(numlist[middle])