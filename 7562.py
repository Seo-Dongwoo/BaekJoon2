from collections import  deque
import sys
dx = [-1,1,2,2,1,-1,-2,-2]
dy = [2,2,1,-1,-2,-2,-1,-1]

def bfs(sx,sy,ax,ay):
    queue = deque()
    queue.append([sx,sy])
    s[sx][sy] = 1

    while queue:
        a,b = queue.popleft()
        if a == ax and b == ay:
            print(s[ax][ay]-1)
            return
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and s[nx][ny] == 0:
                queue.append([nx,ny])
                s[nx][ny] = s[a][b] + 1
T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    ax, ay = map(int, sys.stdin.readline().split())
    sx, sy = map(int, sys.stdin.readline().split())
    s = [[0] * N for i in range(N)]
    bfs(sx,sy,ax,ay)