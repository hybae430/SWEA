def dfs(dep, dest):
    if dep == dest:
        return 0
    print(visited)
    if dep in road.keys():
        for r in road[dep]:
            if r not in visited and r != dest:
                visited.append(r)
                return dfs(r, dest)
            elif r == dest:
                return dfs(r, dest) + 1

road = {'ULSAN': ['BUSAN', 'DAEGU'], 'DAEJEON': ['ULSAN', 'GWANGJU', 'DAEGU'], 'SEOUL': ['DAEJEON', 'ULSAN'], 'GWANGJU': ['BUSAN', 'YEOSU'], 'DAEGU': ['GWANGJU', 'BUSAN'], 'BUSAN': ['YEOSU']}
dep = 'SEOUL'
visited = [dep]
s1 = dfs(dep, 'DAEJEON')
print(s1)