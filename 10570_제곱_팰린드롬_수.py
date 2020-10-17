def pal(num):
    string = str(num)
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True

square = []
for i in range(1001):
    square.append(i * i)

T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B + 1):
        if pal(i):
            if i in square:
                if pal(square.index(i)):
                    cnt += 1
    print('#{} {}'.format(tc, cnt))