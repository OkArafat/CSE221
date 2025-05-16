import os
import heapq
from collections import defaultdict

# Only implement solve(), no main, file, open, input, print, etc.
def solve():
    # read all input from fd 0
    data = os.read(0, 1 << 26).split()
    it = iter(data)

    N = int(next(it))
    M = int(next(it))
    S = int(next(it))
    D = int(next(it))

    # second line u's
    u_list = [int(next(it)) for _ in range(M)]
    # third line v's
    v_list = [int(next(it)) for _ in range(M)]
    # fourth line w's
    w_list = [int(next(it)) for _ in range(M)]

    graph = defaultdict(list)
    for i in range(M):
        u = u_list[i]
        v = v_list[i]
        w = w_list[i]
        graph[u].append((v, w))

    INF = 10**30
    dist = [INF] * (N + 1)
    prev_node = [-1] * (N + 1)

    dist[S] = 0
    pq = [(0, S)]  # (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if dist[v] > nd:
                dist[v] = nd
                prev_node[v] = u
                heapq.heappush(pq, (nd, v))

    # prepare output
    out = []
    if dist[D] == INF:
        out.append(b'-1\n')
    else:
        out.append(str(dist[D]).encode() + b'\n')
        # reconstruct path
        path = []
        cur = D
        while cur != -1:
            path.append(cur)
            cur = prev_node[cur]
        path.reverse()
        out.append(b' '.join(str(x).encode() for x in path) + b'\n')

    os.write(1, b''.join(out))

# call solve directly
solve()
