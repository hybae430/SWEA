T = int(input())

for i in range(1, T + 1):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))

    charge = 0
    tmp = 0
    
    while tmp + K < N:
        if tmp + K in stops:
            charge += 1
            tmp += K
        else:
            idx = 0
            for stop in stops:
                if stop > tmp + K:
                    break
                else:
                    idx += 1
            if idx == 0 or stops[idx - 1] == tmp:
                charge = 0
                break
            else:
                charge += 1
                tmp = stops[idx - 1]
    
    print(f'#{i} {charge}')