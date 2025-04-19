N, M = map(int, input().split())

u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))

graph = {}

for i in range(1, N + 1):
    graph[i] = []
    
for i in range(M):
    u = u_list[i]
    v = v_list[i]
    w = w_list[i]
    graph[u].append((v, w))  

for i in range(1, N + 1):
    print(f"{i}:", end="")
    for v, w in graph[i]:
        print(f" ({v},{w})", end="")
    print()  
