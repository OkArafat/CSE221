import heapq
import sys
from collections import defaultdict
 
def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
 
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    S = int(data[idx]); idx += 1
    D = int(data[idx]); idx += 1
 
    u = list(map(int, data[idx:idx + M])); idx += M
    v = list(map(int, data[idx:idx + M])); idx += M
    w = list(map(int, data[idx:idx + M])); idx += M
 
    graph = defaultdict(list)
    for i in range(M):
        graph[u[i]].append((v[i], w[i]))
 
    dist = [float('inf')] * (N + 1)
    prev = [-1] * (N + 1)
    dist[S] = 0
    pq = [(0, S)]
 
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for nei, weight in graph[node]:
            if dist[nei] > d + weight:
                dist[nei] = d + weight
                prev[nei] = node
                heapq.heappush(pq, (dist[nei], nei))
 
    if dist[D] == float('inf'):
        print(-1)
        return
 
    path = []
    cur = D
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
 
    print(dist[D])
    print(' '.join(map(str, path)))
 
if _name_ == "_main_":
    main()