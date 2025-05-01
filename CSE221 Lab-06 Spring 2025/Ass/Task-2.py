import sys
from collections import deque,defaultdict
input = sys.stdin.readline
n,m = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
color = [-1] * (n + 1)
def bfs(start):
    queue = deque([start])
    color[start] = 0
    count = [1, 0]  
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                color[neighbor] = 1 - color[node]
                count[color[neighbor]] += 1
                queue.append(neighbor)
    return max(count)
result = 0
for i in range(1, n + 1):
    if color[i] == -1:
        result += bfs(i)
print(result)