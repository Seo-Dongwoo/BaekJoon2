from collections import  deque
import sys
N, K = map(int, sys.stdin.readline().split())
MAX = 10 ** 5
graph = [0] * (MAX+1)


def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(graph[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not graph[nx]:
                graph[nx] = graph[x] + 1
                queue.append(nx)

bfs()