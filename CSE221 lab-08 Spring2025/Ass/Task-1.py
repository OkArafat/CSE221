import sys
input = sys.stdin.readline
n,k = map(int, input().split())
parent = list(range(n + 1))
size = [1] * (n + 1)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  
    return parent[x]
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        if size[x_root] < size[y_root]:
            x_root, y_root = y_root, x_root
        parent[y_root] = x_root
        size[x_root] += size[y_root]
    return size[x_root]
for _ in range(k):
    a, b = map(int, input().split())
    print(union(a, b))
