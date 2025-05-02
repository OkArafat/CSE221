import sys
from collections import deque
def solveing():
    N = int(sys.stdin.readline())
    a1,b1,x1,y1 = map(int,sys.stdin.readline().split())
    path=[(-2, -1), (-1, -2), (1, -2), (2, -1),
                  (2, 1), (1, 2), (-1, 2), (-2, 1)]
    show = [[-1] * (N + 1) for z in range(N + 1)]
    q = deque()
    q.append((a1, b1))
    show[a1][b1] = 0    
    while q:
        x,y = q.popleft()
        if x == x1 and y == y1:
            print(show[x][y])
            return
        for dx, dy in path:
            nx = x + dx
            ny = y + dy
            if 1 <= nx <= N and 1 <= ny <= N and show[nx][ny] == -1:
                show[nx][ny] = show[x][y] + 1
                q.append((nx, ny))
    print(-1)
solveing()