n,m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

visited_1 = [0] * (n + 1) 

def has_cycle(start):
    stack_1 = [(start, 0)]
    path = []

    while stack_1:
        
        node,idx = stack_1[-1]
        if visited_1[node] == 0:
            visited_1[node] = 1
            path.append(node)
        neighbors_1 = graph[node]

        if idx < len(neighbors_1):
            neighbor = neighbors_1[idx]
            stack_1[-1] = (node,idx + 1)
            if visited_1[neighbor] == 0:
                stack_1.append((neighbor, 0))
                
            elif visited_1[neighbor] == 1:
                return True  
        else:
            visited_1[node] = 2
            stack_1.pop()
            path.pop()
    return False

for node in range(1, n + 1):
    if visited_1[node] == 0:
        if has_cycle(node):
            print("YES")
            break
else:
    print("NO")
