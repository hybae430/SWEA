def traverse(node):
    if node == 0:
        return 0
    return traverse(L[node]) + traverse(R[node]) + 1

def grandp(node, g_list):
    g_list.append(P[node])
    if P[node] == 1:
        return
    return grandp(P[node], g_list)

T = int(input())
for tc in range(1, T + 1):
    V, E, X, Y = map(int, input().split())
    infos = list(map(int, input().split()))
    P, L, R = [0] * (E + 2), [0] * (E + 2), [0] * (E + 2)
    grand_X, grand_Y = [], []
    for i in range(0, E * 2, 2):
        p, c = infos[i], infos[i + 1]
        if L[p]:
            R[p] = c
        else:
            L[p] = c
        P[c] = p
    grandp(X, grand_X)
    grandp(Y, grand_Y)
    for n in grand_X:
        if n in grand_Y:
            node = n
            break
    print('#{} {} {}'.format(tc, node, traverse(node)))