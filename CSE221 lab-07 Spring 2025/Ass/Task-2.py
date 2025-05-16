import os
from collections import defaultdict
def solve():
    data = os.read(0, 1 << 26).split()
    it = iter(data)
    N = int(next(it)); M = int(next(it))
    S = int(next(it)); T = int(next(it))    
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        graph[u].append((v, w))
    class MinHeap:
        def __init__(self):
            self.h = []
        def push(self, item):
            self.h.append(item)
            i = len(self.h) - 1
            while i > 0:
                p = (i - 1) // 2
                if self.h[p][0] <= self.h[i][0]:
                    break
                self.h[p], self.h[i] = self.h[i], self.h[p]
                i = p
        def pop(self):
            last = self.h.pop()
            if not self.h:
                return last
            ret = self.h[0]
            self.h[0] = last
            n = len(self.h)
            i = 0
            while True:
                l = 2*i + 1
                r = 2*i + 2
                smallest = i
                if l < n and self.h[l][0] < self.h[smallest][0]:
                    smallest = l
                if r < n and self.h[r][0] < self.h[smallest][0]:
                    smallest = r
                if smallest == i:
                    break
                self.h[i], self.h[smallest] = self.h[smallest], self.h[i]
                i = smallest
            return ret
        def __bool__(self):
            return bool(self.h)
    INF = 10**30
    distA = [INF] * (N+1)
    distB = [INF] * (N+1)
    distA[S] = 0
    distB[T] = 0
    best_time = INF
    best_node = -1
    heap = MinHeap()
    heap.push((0, S, 0))
    heap.push((0, T, 1))
    while heap:
        t,u,who=heap.pop()
        if who == 0:
            if t > distA[u]:
                continue
        else:
            if t > distB[u]:
                continue
        other_dist = distB[u] if who == 0 else distA[u]
        if other_dist < INF:
            meet_time = t if t > other_dist else other_dist
            if meet_time < best_time or (meet_time == best_time and u < best_node):
                best_time = meet_time
                best_node = u
        if heap and heap.h[0][0] >= best_time:
            break
        for v,w in graph[u]:
            nt = t + w
            if who == 0:
                if nt < distA[v]:
                    distA[v] = nt
                    heap.push((nt, v, 0))
            else:
                if nt < distB[v]:
                    distB[v] = nt
                    heap.push((nt, v, 1))
    out = []
    if best_node == -1:
        out.append(b'-1\n')
    else:
        out.append(str(best_time).encode())
        out.append(b' ')
        out.append(str(best_node).encode())
        out.append(b'\n')
    os.write(1, b''.join(out))
solve()
