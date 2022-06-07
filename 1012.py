import sys
from collections import deque
T = int(sys.stdin.readline())
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] =0
                queue.append((nx,ny))
    return

for i in range(T):
    bug = 0
    N, M, K = map(int, sys.stdin.readline().split())
    graph = [[0]*M for _ in range(N)]

    for j in range(K):
        x, y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1

    for a in range(N):
        for b in range(M):
            if graph[a][b] == 1:
                bfs(a,b)
                bug += 1
    print(bug)