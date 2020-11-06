# 최대 상금
def dfs(cnt):
    global ans
    if cnt == swap:
        ans = max(int(''.join(list(map(str, cards)))), ans)
        return
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            cards[i], cards[j] = cards[j], cards[i]
            tmp = int(''.join(list(map(str, cards))))
            if (tmp, cnt + 1) not in visited:
                visited.append((tmp, cnt + 1))
                dfs(cnt + 1)
            cards[i], cards[j] = cards[j], cards[i]

T = int(input())
for tc in range(1, T + 1):
    cards, swap = map(int, input().split())
    cards = list(str(cards))
    ans, flag = 0, False
    visited = []
    cards = list(map(int, cards))
    dfs(0)
    print('#{} {}'.format(tc, ans))