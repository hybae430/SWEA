numlist = [i for i in range(1, 11)]
N = len(numlist)
sel = [0] * N
psets = []
ans = []

def powerset(idx):
    if idx == N:
        tmp = []
        for i in range(N):
            if sel[i]:
                tmp.append(numlist[i])
        psets.append(tmp)
        return

    sel[idx] = 1
    powerset(idx + 1)
    sel[idx] = 0
    powerset(idx + 1)

powerset(0)
for ps in psets:
    if sum(ps) == 10:
        ans.append(ps)
print(ans)