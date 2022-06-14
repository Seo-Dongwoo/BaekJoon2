import sys
import heapq
N, M = map(int, sys.stdin.readline().split())
INF = sys.maxsize
start_node = int(sys.stdin.readline())
distances = [INF] *(N + 1)
heap = []
graph = [[] for _ in range(N+1)]

def aijkstra(start):
    distances[start] = 0
    heapq.heappush(heap,(0,start))
    while heap:
        wei, now = heapq.heappop(heap)
        if distances[now] < wei:
            continue

        for w, next_node in graph[now]:
            next_wei = w + wei
            if next_wei < distances[next_node]:
                distances[next_node] = next_wei
                heapq.heappush(heap, (next_wei,next_node))

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w,v))

aijkstra(start_node)
for i in range(1, N+1):
    print("INF" if distances[i] == INF else distances[i])

