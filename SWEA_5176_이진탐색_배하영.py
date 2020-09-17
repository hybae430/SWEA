class Tree:
    def __init__(self, N):
        self.tree_list = [0] * (N + 1)
        self.cnt = 1
        self.N = N
        self.insert(1)

    def insert(self, num):
        if num <= N:
            self.insert(num * 2)
            self.tree_list[num] = self.cnt
            self.cnt += 1
            self.insert(num * 2 + 1)

    def toString(self):
        return ' '.join(self.tree_list[1], self.tree_list[N // 2])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mytree = Tree(N)
    print('#{} {}'.format(tc, mytree.toString()))