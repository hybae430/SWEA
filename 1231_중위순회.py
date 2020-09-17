def inorder(n):
    if bin_tree[n * 2]:
        inorder(n * 2)
    in_trav.append(infos[n][1])
    if bin_tree[n * 2 + 1]:
        inorder(n * 2 + 1)

for tc in range(1, 11):
    N = int(input())
    bin_tree = [0] * N ** 2
    in_trav, infos = [], [[]]
    for i in range(N):
        info = list(input().split())
        infos.append(info)
        if len(info) > 2:
            for j in range(2, len(info)):
                parent = int(info[0])
                child = int(info[j])

                if parent not in bin_tree:
                    idx = 0
                else:
                    idx = bin_tree.index(parent)

                if idx == 0:
                    bin_tree[1], bin_tree[2] = parent, child
                else:
                    if bin_tree[idx * 2] == 0:
                        bin_tree[idx * 2] = child
                    else:
                        bin_tree[idx * 2 + 1] = child
    inorder(1)
    print('#{} {}'.format(tc, ''.join(in_trav)))