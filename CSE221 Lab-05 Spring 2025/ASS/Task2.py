import sys
from collections import deque
sys.setrecursionlimit(2*10**5)

n,m = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

graph_1 =[[] for _ in range(n + 1)]
for u,v in zip(u_list, v_list):
    graph_1[u].append(v)
    graph_1[v].append(u)
for g in graph_1:
    g.sort()
visited_1 = [False] * (n + 1)
result_01 =[]
def dfs(start):
    stack_1 = [start]
    while stack_1:
        node = stack_1.pop()
        if not visited_1[node]:
            visited_1[node] = True
            result_01.append(node)
            stack_1.extend(reversed(graph_1[node]))
dfs(1)
print(*result_01)
