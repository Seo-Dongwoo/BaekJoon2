from collections import  deque
import sys
N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = [] # 단지별로 집의 수를 리스트로 저장

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count = 1 # 각 단지의 집의 수

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i] # dx, dy의 배열을 돌면서 상하좌우 같은 것 추가
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(i,j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])