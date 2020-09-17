for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))
    while N > 0:
        if max(box) - min(box) < 2:
            break
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1
        N -= 1
    # 끝까지 돌았을 경우 max와 min이 또 바뀔 수도 있기 때문
    print('#{} {}'.format(tc, max(box) - min(box)))