import sys
import heapq
from collections import defaultdict
 
def dijkstra(start, graph, N):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for nei, weight in graph[node]:
            if dist[nei] > d + weight:
                dist[nei] = d + weight
                heapq.heappush(pq, (dist[nei], nei))
    return dist
 
def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
 
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    S = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
 
    graph = defaultdict(list)
 
    for _ in range(M):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        graph[u].append((v, w))
 
   
    dist_from_S = dijkstra(S, graph, N)
 
    dist_from_T = dijkstra(T, graph, N)
 
 
    min_time = float('inf')
    meet_node = -1
 
    for i in range(1, N + 1):
        max_time = max(dist_from_S[i], dist_from_T[i])
        if dist_from_S[i] != float('inf') and dist_from_T[i] != float('inf'):
            if max_time < min_time or (max_time == min_time and i < meet_node):
                min_time = max_time
                meet_node = i
 
    if meet_node == -1:
        print(-1)
    else:
        print(min_time, meet_node)
 
if _name_ == "_main_":
    main()