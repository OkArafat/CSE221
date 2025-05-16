import os
def solve():
    data = os.read(0, 1 << 26).split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    u = [0]*m
    for i in range(m): 
        u[i] = int(next(it))
    v = [0]*m
    for i in range(m): 
        v[i] = int(next(it))
    w = [0]*m
    for i in range(m): 
        w[i] = int(next(it))
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        graph[u[i]].append((v[i], w[i]))
    inf_1 = 10**30
    dist0 = [inf_1] * (n+1)
    dist1 = [inf_1] * (n+1)
    heap = []
    def push(item):
        heap.append(item)
        i = len(heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if heap[p][0] <= heap[i][0]:
                break
            heap[p], heap[i] = heap[i], heap[p]
            i = p
    def pop():
        last = heap.pop()
        if not heap: return last
        ret = heap[0]
        heap[0] = last
        n0 = len(heap)
        i = 0
        while True:
            l = 2*i + 1; r = 2*i + 2; s = i
            if l < n0 and heap[l][0] < heap[s][0]: s = l
            if r < n0 and heap[r][0] < heap[s][0]: s = r
            if s == i: 
                break
            heap[i],heap[s] = heap[s], heap[i]
            i = s
        return ret
    for to, weight in graph[1]:
        p = weight & 1
        if p == 0 and weight < dist0[to]:
            dist0[to] = weight
            push((weight,to,0))
        if p == 1 and weight < dist1[to]:
            dist1[to] = weight
            push((weight,to,1))
    while heap:
        cost,node,par = pop()
        if par == 0:
            if cost != dist0[node]:
                continue
        else:
            if cost != dist1[node]:
                continue
        for to, weight in graph[node]:
            np = weight & 1
            if np == par:
                continue
            nc = cost + weight
            if np == 0:
                if nc < dist0[to]:
                    dist0[to] = nc
                    push((nc, to, 0))
            else:
                if nc < dist1[to]:
                    dist1[to] = nc
                    push((nc,to,1))
    res = dist0[n] if dist0[n] < dist1[n] else dist1[n]
    if res >= inf_1: res = -1
    os.write(1, (str(res) + "\n").encode())
solve()
