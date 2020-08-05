T = int(input())
ans = []

def printdata(mylist):
    for i in range(len(mylist)):
        print(mylist[i], end = " ")
    print()

def pascal(n):
    start = 1
    res = [1, 1]
    while start <= n:
        if start == 1:
            ans.append([1])
        elif start == 2:
            ans.append(res)
        else:
            tmp = [1, 1]
            for i in range(len(res) - 1):
                tmp.insert(i + 1, res[i] + res[i + 1])
            ans.append(tmp)
            res = tmp
        start += 1

pascal(10)

for i in range(1, T + 1):
    N = int(input())
    print(f'#{i} {ans[N - 1]}')

'''
T = int(input())

def printdata(mylist):
    for i in range(len(mylist)):
        print(mylist[i], end = " ")
    print()

def pascal(n):
    start = 1
    res = [1, 1]
    while start <= n:
        if start == 1:
            print(1)
        elif start == 2:
            printdata(res)
        else:
            tmp = [1, 1]
            for i in range(len(res) - 1):
                tmp.insert(i + 1, res[i] + res[i + 1])
            printdata(tmp)
            res = tmp
        start += 1

for i in range(1, T + 1):
    N = int(input())
    print('#{}'.format(i))
    pascal(N)
'''