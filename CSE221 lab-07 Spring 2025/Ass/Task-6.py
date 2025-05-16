import os

def ok():
    data = os.read(0, 1 << 26).split()
    it = iter(data)
    n= int(next(it))
    m = int(next(it))
    s = int(next(it))
    d = int(next(it))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it)) 
        w = int(next(it))
        graph[u].append((v,w))
        graph[v].append((u,w))
    inf_1 = 10**30
    dist0 = [inf_1] * (n+1)
    dist1 = [inf_1] * (n+1)
    dist0[s] = 0
    heap = []
    def push(item):
        heap.append(item)
        i = len(heap)-1
        while i>0:
            p = (i-1)//2
            if heap[p][0] <= heap[i][0]:
                break
            heap[p],heap[i] = heap[i], heap[p]
            i = p
    def pop():
        last = heap.pop()
        if not heap: return last
        ret = heap[0]
        heap[0] = last
        n0 = len(heap); i = 0
        while True:
            l = 2*i+1
            r = 2*i+2
            s0 = i
            if l<n0 and heap[l][0] < heap[s0][0]: s0 = l
            if r<n0 and heap[r][0] < heap[s0][0]: s0 = r
            if s0 == i: 
                break
            heap[i], heap[s0] = heap[s0], heap[i]
            i = s0
        return ret
    push((0, s))
    while heap:
        cost, u = pop()
        if cost > dist1[u]:
            continue
        for v, w in graph[u]:
            nc = cost + w
            if nc < dist0[v]:
                dist1[v] = dist0[v]
                dist0[v] = nc
                push((nc, v))
                if dist1[v] < inf_1:
                    push((dist1[v], v))
            elif dist0[v] < nc < dist1[v]:
                dist1[v] = nc
                push((nc, v))
    ans = dist1[d]
    if ans >= inf_1:
        os.write(1, b'-1\n')
    else:
        os.write(1, (str(ans) + '\n').encode())
ok()
