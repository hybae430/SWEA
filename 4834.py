from collections import Counter

T = int(input())

for i in range(1, T + 1):
    N = int(input())
    a = list(input())
    order = Counter(a).most_common()
    maximum = order[0][1]
    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
        else:
            break
    freq = max(modes)
    print(f'#{i} {freq} {maximum}')