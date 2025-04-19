from collections import deque
n,m,s,d = map(int, input().split())
u_1 = list(map(int, input().split()))
v_1 = list(map(int, input().split()))
graph_1 = [[] for _ in range(n + 1)]
for i in range(m):
    u = u_1[i]
    v = v_1[i]
    graph_1[u].append(v)
    graph_1[v].append(u)
for neighbors in graph_1:
    neighbors.sort()
visited = [False] * (n + 1)
distance = [-1] * (n + 1)
parent = [-1] * (n + 1)
queue_1 = deque([s])
visited[s] = True
distance[s] = 0
while queue_1:
    u = queue_1.popleft()
    for v in graph_1[u]:
        if not visited[v]:
            visited[v] = True
            distance[v] = distance[u] + 1
            parent[v] = u
            queue_1.append(v)

if not visited[d]:
    print(-1)
else:
    path_1 = []
    while d != -1:
        path_1.append(d)
        d = parent[d]
    path_1.reverse()
    print(len(path_1) - 1)
    print(*path_1)
