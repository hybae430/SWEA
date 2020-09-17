T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(input())
    cnt = {}
    for card in cards:
        cnt[card] = cnt.get(card, 0) + 1
    ans = sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)[0]
    print('#{} {} {}'.format(tc, ans[0], ans[1]))
