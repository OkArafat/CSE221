import sys
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))  
        self.rank = [0] * (size + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]   
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        return True

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    N, M = map(int, input[ptr:ptr+2])
    ptr +=2
    edges = []
    for _ in range(M):
        u, v, w = map(int, input[ptr:ptr+3])
        ptr +=3
        edges.append((u, v, w))
    
    edges_sorted = sorted(edges, key=lambda x: x[2])

    uf = UnionFind(N)
    mst_edges = []
    mst_cost = 0
    for u, v, w in edges_sorted:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            mst_cost += w
    
    if len(mst_edges) != N - 1:
        print(-1)
        return
 
    second_best = float('inf')
    for i in range(len(mst_edges)):
        uf_second = UnionFind(N)
        cost = 0
        count = 0

        for j in range(len(mst_edges)):
            if j == i:
                continue
            u, v, w = mst_edges[j]
            if uf_second.union(u, v):
                cost += w
                count += 1
        if count != N - 1:
            u_remove, v_remove, w_remove = mst_edges[i]
            uf_second = UnionFind(N)

            for j in range(len(mst_edges)):
                if j == i:
                    continue
                u, v, w = mst_edges[j]
                uf_second.union(u, v)
            min_add = float('inf')
            for u, v, w in edges_sorted:
                if uf_second.find(u) != uf_second.find(v):
                    if w < min_add:
                        min_add = w
            if min_add != float('inf'):
                total_cost = cost + min_add
                if total_cost > mst_cost and total_cost < second_best:
                    second_best = total_cost
        else:
            if cost > mst_cost and cost < second_best:
                second_best = cost

    adj = defaultdict(list)
    edge_info = {}  
    for u, v, w in mst_edges:
        adj[u].append(v)
        adj[v].append(u)
        edge_info[(u, v)] = w
        edge_info[(v, u)] = w

    non_mst_edges = [edge for edge in edges if (edge[0], edge[1]) not in edge_info and (edge[1], edge[0]) not in edge_info]
    
    for u, v, w in non_mst_edges:
        parent = {}
        visited = {}
        queue = []
        start = u
        end = v
        queue.append(start)
        visited[start] = True
        found = False
        parent[start] = None
        while queue and not found:
            current = queue.pop(0)
            for neighbor in adj[current]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    parent[neighbor] = current
                    queue.append(neighbor)
                    if neighbor == end:
                        found = True
                        break
        if found:
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            max_edge = 0
            for i in range(len(path) - 1):
                a = path[i]
                b = path[i+1]
                weight = edge_info[(a, b)]
                if weight > max_edge:
                    max_edge = weight
            total_cost = mst_cost + w - max_edge
            if total_cost > mst_cost and total_cost < second_best:
                second_best = total_cost
    
    if second_best != float('inf'):
        print(second_best)
    else:
        print(-1)

solve()