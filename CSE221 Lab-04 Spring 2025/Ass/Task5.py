def solve():
    
    N,M = map(int, input().split())
    
    U =list(map(int, input().split()))
    
    V =list(map(int, input().split()))
    
    inde_gree = [0] * (N + 1)
    
    out_degree = [0] * (N + 1)
    
    for i in range(M):
        
        out_degree[U[i]] += 1
        
        inde_gree[V[i]] += 1

    for i in range(1, N + 1):
        
        print(inde_gree[i] - out_degree[i], end=' ')
    print() 

solve()
