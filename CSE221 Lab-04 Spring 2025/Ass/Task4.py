N,M = map(int, input().split())

U = list(map(int, input().split()))
V = list(map(int, input().split()))

degre = [0]*(N + 1)  
for i in range(M):
    degre[U[i]] += 1  
    degre[V[i]] += 1 

odd_count = 0
for i in range(1, N + 1):
    if degre[i] % 2 == 1:
        odd_count += 1

if odd_count == 0 or odd_count == 2:
    
    print("YES")
else:
    print("NO")
