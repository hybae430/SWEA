T = int(input())

# def dfs(N):
#     global cnt
#
#     for child in tree_list[N]:
#         if child not in visited:
#             cnt += 1
#             visited.append(child)
#             dfs(child)

def traverse(node):
    if node == 0:
        return 0
    return traverse(L[node]) + traverse(R[node]) + 1

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    nums = list(map(int, input().split()))
    P, L, R = [0] * (E + 2), [0] * (E + 2), [0] * (E + 2)
    for i in range(0, E * 2, 2):
        p, c = nums[i], nums[i + 1]
        if L[p]:
            R[p] = c
        else:
            L[p] = c
        P[c] = p
    print('#{} {}'.format(tc, traverse(N)))