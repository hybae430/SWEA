T = int(input())
prime_num = [2, 3, 5, 7, 11]
for tc in range(1, T + 1):
    ans = [0] * 5
    N = int(input())
    for i in range(len(prime_num)):
        while not N % prime_num[i] and N != 1:
            ans[i] += 1
            N //= prime_num[i]
    print(f'#{tc}', end = " ")
    for num in ans:
        print(num, end = " ")
    print()