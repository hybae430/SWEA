def postorder(n):
    if bin_tree[n * 2]:
        postorder(n * 2)
    if bin_tree[n * 2 + 1]:
        postorder(n * 2 + 1)
    post_trav.append(infos[bin_tree[n]][1])

def cal(my_list):
    func = ['+', '-', '/', '*']
    for com in my_list:
        if com not in func:
            st.append(com)
        else:
            b, a = int(st.pop()), int(st.pop())
            if com == '+':
                st.append(a + b)
            elif com == '-':
                st.append(a - b)
            elif com == '*':
                st.append(a * b)
            elif com == '/':
                st.append(a // b)

for tc in range(1, 11):
    N = int(input())
    bin_tree = [0] * N ** 2
    post_trav, infos, st = [], [[]], []
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
    postorder(1)
    cal(post_trav)

    print('#{} {}'.format(tc, st[0]))