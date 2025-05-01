import sys
sys.setrecursionlimit(10**6)

def calculate_subtree_sizes(N, R, adj):

    subtree_size = [0] * (N + 1)
    stack = [(R, -1)]  
    post_order = [] 
    
    while stack:
        node, parent = stack.pop()
        post_order.append((node, parent))  
        for neighbor in adj[node]:
            if neighbor != parent:
                stack.append((neighbor, node))
    for node, parent in reversed(post_order):
        subtree_size[node] = 1 
        for neighbor in adj[node]:
            if neighbor != parent:
                subtree_size[node] += subtree_size[neighbor]
    
    return subtree_size

N, R = map(int, input().split())  
adj = [[] for _ in range(N + 1)] 
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

subtree_size = calculate_subtree_sizes(N, R, adj)

Q = int(input())

for _ in range(Q):
    X = int(input())
    print(subtree_size[X])
