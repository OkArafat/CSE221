class DSU:
    def __init__(self, n):
        self.parentss = list(range(n + 1))
        self.rank = [1] * (n + 1)
    def get(self, x):
        while self.parentss[x] != x:
            self.parentss[x] = self.parentss[self.parentss[x]]
            x = self.parentss[x]
        return x
    def merge(self, x, y):
        x_root_1 = self.get(x)
        y_root_1 = self.get(y)
        if x_root_1 == y_root_1:
            return False
        if self.rank[x_root_1] < self.rank[y_root_1]:
            x_root_1, y_root_1 = y_root_1, x_root_1
        self.parentss[y_root_1] = x_root_1
        self.rank[x_root_1] += self.rank[y_root_1]
        return True
def main():
    from sys import stdin
    red_12 = stdin.read().split()
    n = int(red_12[0])
    m = int(red_12[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(red_12[idx])
        v = int(red_12[idx + 1])
        w = int(red_12[idx + 2])
        edges.append((w, u, v))
        idx += 3
    edges.sort()
    dsu = DSU(n)
    fullcost = 0
    for w, u, v in edges:
        if dsu.merge(u, v):
            fullcost += w
    print(fullcost)
main()