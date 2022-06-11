import sys
T = int(sys.stdin.readline())

def bfs(node):
    queue = [node]
    visited[node] = 1
    while queue:
        node = queue[0]
        queue.pop(0)
        next = arr[node]
        if visited[next] == 0:
            visited[next] = 1
            queue.append(next)
    return 1


for i in range(T):
    answer = 0
    N = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] * (N + 1)

    for i in range(1, N + 1):
        if visited[i] == 0:
            answer += bfs(i)
    print(answer)
