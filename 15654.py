import sys
N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
L.sort()
visited = [False]*N
s = []

def dfs(depth):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(N):
        if not visited[i]:
            s.append(L[i])
            visited[i] = True
            dfs(depth+1)
            s.pop()
            visited[i] = False
dfs(1)

