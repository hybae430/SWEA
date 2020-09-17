class Tree:
    def __init__(self, N):
        self.tree_list = [0] * (N + 1)
        self.N = N

    def add(self, node):
        if node * 2 > N:
            self.branch += self.tree_list[node]
        else:
            self.add(node * 2)
            if node * 2 != N:
                self.add(node * 2 + 1)

    def insert(self, node, num):
        self.tree_list[node] = num

    def res(self, L):
        self.branch = 0
        self.add(L)
        return self.branch

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = Tree(N)
    for i in range(M):
        node, num = map(int, input().split())
        tree.insert(node, num)
    print('#{} {}'.format(tc, tree.res(L)))