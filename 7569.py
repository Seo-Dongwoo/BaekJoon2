from collections import deque

m, n, h = map(int, input().split())

tomato1 = [[list(map(int, input().split())) for i in range(n)] for depth in range(h)]

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato1[i][j][k] == 1:
                queue.append([i, j, k])
while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nz = z + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if tomato1[nz][nx][ny] == 0:
                tomato1[nz][nx][ny] = tomato1[z][x][y] + 1
                queue.append([nz, nx, ny])

flag = False
for i in tomato1:
    for j in i:
        for k in j:
            if k == 0:
                flag = True
                break

if flag:
    print(-1)
else:
    day = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                day = max(day, tomato1[i][j][k])
    print(day - 1)