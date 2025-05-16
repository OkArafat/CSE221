import os
def solve():
    data = os.read(0, 1 << 26).split()
    it = iter(data)
    New = int(next(it)); M = int(next(it))
    ok = [[] for _ in range(New+1)]
    for _ in range(M):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        ok[u].append((v,w))
        ok[v].append((u,w))
    INF_1 = 10**30
    dnger = [INF_1] * (New+1)
    dnger[1] = 0
    heap = []
    def heap_push(item):
        heap.append(item)
        i = len(heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if heap[p][0] <= heap[i][0]:
                break
            heap[p],heap[i] = heap[i], heap[p]
            i = p
    def heap_pop():
        last = heap.pop()
        if not heap:
            return last
        ret = heap[0]
        heap[0] = last
        n = len(heap)
        i = 0
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            s = i
            if l < n and heap[l][0] < heap[s][0]:
                s = l
            if r < n and heap[r][0] < heap[s][0]:
                s = r
            if s == i:
                break
            heap[i], heap[s] = heap[s], heap[i]
            i = s
        return ret
    heap_push((0, 1))
    while heap:
        d, u = heap_pop()
        if d > dnger[u]:
            continue
        for v, w in ok[u]:
            nd = w if w > d else d
            if nd < dnger[v]:
                dnger[v] = nd
                heap_push((nd, v))
    out = []
    for i in range(1, New+1):
        if dnger[i] == INF_1:
            out.append(b'-1')
        else:
            out.append(str(dnger[i]).encode())
    os.write(1, b' '.join(out) + b'\n')
solve()
