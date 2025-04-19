r,h = map(int, input().split())

grid = [list(input().strip()) for _ in range(r)]
def dfs_iterative(x, y):
    stack_1 = [(x, y)]
    diamonds_1 = 0

    while stack_1:
        cx, cy = stack_1.pop()

        if cx < 0 or cx >= r or cy < 0 or cy >= h:
            continue
        
        if grid[cx][cy] == '#' or grid[cx][cy] == 'V':
            continue

        if grid[cx][cy] == 'D':
            diamonds_1 += 1

        grid[cx][cy] = 'V'

        for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            stack_1.append((cx+dx,cy+dy))
    return diamonds_1

maxdiamonds_1 = 0

for i in range(r):
    for j in range(h):
        if grid[i][j] != '#' and grid[i][j] != 'V':
            maxdiamonds_1 = max(maxdiamonds_1, dfs_iterative(i, j))

print(maxdiamonds_1)
