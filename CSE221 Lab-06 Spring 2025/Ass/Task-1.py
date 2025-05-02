import heapq
from collections import defaultdict

n, m = map(int,input().split())
graph = defaultdict(list)
in_degree = [0]*(n + 1)

for l in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    in_degree[v] += 1

heap_a = []

for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(heap_a, i)

result = []
while heap_a:
    u = heapq.heappop(heap_a)
    result.append(u)
    for v in sorted(graph[u]):
        
        in_degree[v] -= 1
        if in_degree[v] == 0:
            heapq.heappush(heap_a, v)

if len(result) == n:
    print(' '.join(map(str, result)))
    
else:
    print(-1)
