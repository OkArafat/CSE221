from collections import deque
def bfs(start,graph,n):
    dist_1 = [-1] * (n + 1)
    parent_1 = [-1] * (n + 1)
    queue = deque()
    queue.append(start)
    dist_1[start] = 0

    for u in queue:
        for v in graph[u]:
            if dist_1[v] == -1:
                dist_1[v] = dist_1[u] + 1
                parent_1[v] = u
                queue.append(v)
    return dist_1, parent_1
n,m,s,d,k = map(int,input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
def find_path(start,end,graph,n):
    dist_1 = [-1] * (n + 1)
    parent_1 = [-1] * (n + 1)
    queue = deque([start])
    dist_1[start] = 0
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist_1[v] == -1:
                dist_1[v] = dist_1[u] + 1
                parent_1[v] = u
                queue.append(v)
                if v==end:
                    break
    if dist_1[end] == -1:
        return None
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent_1[cur]
    path.reverse()
    return path

path_s_k = find_path(s, k, graph, n)

path_k_d = find_path(k, d, graph, n)
if not path_s_k or not path_k_d:
    print(-1)
else:
    full_path = path_s_k + path_k_d[1:]
    print(len(full_path) - 1)
    print(" ".join(map(str, full_path)))