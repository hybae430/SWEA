class Tree:
    def __init__(self):
        self.tree_list = [0]

    def sort(self, N):
        if N >= 2:
            if self.tree_list[N] < self.tree_list[N // 2]:
                self.tree_list[N], self.tree_list[N // 2] = self.tree_list[N // 2], self.tree_list[N]
                self.sort(N // 2)

    def insert(self, num):
        N = len(self.tree_list)
        self.tree_list.append(num)
        self.sort(N)

    def add(self, N):
        if N <= 1:
            return self.tree_list[N]
        else:
            return self.tree_list[N] + self.add(N // 2)

    def res(self):
        N = len(self.tree_list) - 1
        if N >= 2:
            return self.add(N // 2)
        else:
            return 0

T = int(input())
for tc in range(1, T + 1):
    N = input()
    infos = list(map(int, input().split()))
    tree = Tree()
    for info in infos:
        tree.insert(info)
    print('#{} {}'.format(tc, tree.res()))