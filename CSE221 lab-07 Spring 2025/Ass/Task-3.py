import sys
import heapq
from collections import defaultdict
 
def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
 
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
 
    graph = defaultdict(list)
    for _ in range(M):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        graph[u].append((v, w))
        graph[v].append((u, w))  
 
   
    danger = [float('inf')] * (N + 1)
    danger[1] = 0  
    pq = [(0, 1)] 
    while pq:
        d, node = heapq.heappop(pq)
        if d > danger[node]:
            continue
        for nei, w in graph[node]:
            new_danger = max(d, w)
            if new_danger < danger[nei]:
                danger[nei] = new_danger
                heapq.heappush(pq, (new_danger, nei))
 
    result = []
    for i in range(1, N + 1):
        if danger[i] == float('inf'):
            result.append("-1")
        else:
            result.append(str(danger[i]))
 
    print(' '.join(result))
 
if _name_ == "_main_":
    main()