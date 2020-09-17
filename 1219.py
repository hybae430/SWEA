for tc in range(1, 11):
    tcn, E = map(int, input().split())
    graph = {}
    visited = []
    res=0
    arrows = list(map(int, input().split()))
    for j in range(0, E * 2, 2):
        if arrows[j] in graph:
            graph[arrows[j]].append(arrows[j + 1])
        else:
            graph[arrows[j]] = [arrows[j + 1]]
    st = []
    st.extend(graph[0])
    while st:
        x = st.pop()
        if x in visited:
            continue;
        else:
            visited.append(x)
        if x == 99:
            res = 1
            break
        elif graph.get(x) == None:
            continue
        else:
            st.extend(graph[x])
    print("#{} {}".format(tc, res))
