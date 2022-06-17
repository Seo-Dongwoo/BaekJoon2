from collections import deque

n = int(input())

graph = []
graph_red = [['0'] * n for i in range(n)]

for i in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph_red[i][j] = 'R'
        else:
            graph_red[i][j] = graph[i][j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b, graph, color):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = '0'

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color:
                graph[nx][ny] = '0'
                queue.append((nx, ny))


cnt = 0
cntRed = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] in 'RGB':
            bfs(i, j, graph, graph[i][j])
            cnt += 1

        if graph_red[i][j] in 'RB':
            bfs(i, j, graph_red, graph_red[i][j])
            cntRed += 1

print(cnt, cntRed)