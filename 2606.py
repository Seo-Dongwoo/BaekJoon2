import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
visited = [0] * (N+1)

def dfs(graph, start_node):
    global cnt
    visited[start_node] = 1
    for i in graph[start_node]:
        if visited[i] == 0:
            dfs(graph, i)
            cnt += 1


dfs(graph, 1)
print(cnt)