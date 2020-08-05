N = int(input())
t = ['3', '6', '9']
for i in range(1, N + 1):
    num = str(i)
    cnt = 0
    for j in range(len(num)):
        if num[j] in t:
            cnt += 1
    if cnt == 0:
        print(num, end = " ")
    else:
        print('-' * cnt, end = " ")