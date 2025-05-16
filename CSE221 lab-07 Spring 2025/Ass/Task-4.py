import os

def res():
    information = os.read(0, 1 << 26).split()
    t = iter(information)
    N = int(next(t)); M = int(next(t)); S = int(next(t)); D = int(next(t))
    ok = [0]*(N+1)
    for i in range(1, N+1):
        ok[i] = int(next(t))
    graph_1=[[] for _ in range(N+1)]
    for _ in range(M):
        u = int(next(t)); v = int(next(t))
        graph_1[u].append(v)
    inf_1 = 10**30
    dist = [inf_1]*(N+1)
    dist[S] = ok[S]
    heap = []
    def push(item):
        heap.append(item)
        i = len(heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if heap[p][0] <= heap[i][0]: break
            heap[p], heap[i] = heap[i], heap[p]
            i = p
    def pop():
        last = heap.pop()
        if not heap:
            return last
        ret = heap[0]
        heap[0] = last
        n = len(heap); i = 0
        while True:
            l = 2*i + 1; r = 2*i + 2; s = i
            if l < n and heap[l][0] < heap[s][0]: s = l
            if r < n and heap[r][0] < heap[s][0]: s = r
            if s == i: break
            heap[i], heap[s] = heap[s], heap[i]
            i = s
        return ret
    push((dist[S], S))
    while heap:
        cost, u = pop()
        if cost > dist[u]: continue
        for v in graph_1[u]:
            nc = cost + ok[v]
            if nc < dist[v]:
                dist[v] = nc
                push((nc, v))
    out = []
    if dist[D] == inf_1:
        out.append(b'-1')
    else:
        out.append(str(dist[D]).encode())
    out.append(b'\n')
    os.write(1, b''.join(out))
res()
