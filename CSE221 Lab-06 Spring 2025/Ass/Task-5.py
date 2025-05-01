from collections import deque, defaultdict
def find_farthest_node(start, graph):
    visited = set()
    queue = deque([(start, 0)])
    first_node = start
    max_distanc = 0
    while queue:
        node,dist = queue.popleft()
        if dist > max_distanc:
            max_distanc = dist
            first_node = node
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))    
    return first_node,max_distanc

def find_diameter(n,edges):
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    far_node, _ = find_farthest_node(1, graph)
    other_node, diameterlength = find_farthest_node(far_node, graph)
    return diameterlength,far_node,other_node
if __name__ == "__main__":
    n = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    length, node_a, node_b = find_diameter(n, edges)
    print(length)
    print(node_a, node_b)