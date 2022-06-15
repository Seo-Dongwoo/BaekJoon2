import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
count = 0

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            bfs(i)
            count += 1
print(count)