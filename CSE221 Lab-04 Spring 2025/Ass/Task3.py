N = int(input())

matrix = [[0] * N for _ in range(N)]

for i in range(N):
    data = list(map(int, input().split()))
    k = data[0]           
    neighbors = data[1:]  
    for j in neighbors:
        matrix[i][j] = 1  
for row in matrix:
    print(" ".join(map(str, row)))
