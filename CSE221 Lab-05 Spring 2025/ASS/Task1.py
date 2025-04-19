from collections import deque
n, m = map(int,input().split())
graph = [[] for l in range(n + 1)]
for l in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited_1 = [False]*(n + 1)
queue = deque()
bfs_order = []
queue.append(1)
visited_1[1] = True
while queue:
    node_1 = queue.popleft()
    bfs_order.append(node_1)

    for neighbor_1 in sorted(graph[node_1]): 
        if not visited_1[neighbor_1]:
            visited_1[neighbor_1] = True
            queue.append(neighbor_1)
            
print(" ".join(map(str,bfs_order)))
