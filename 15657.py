import sys
N, M = map(int, sys.stdin.readline().split())
L = sorted(map(int, sys.stdin.readline().split()))
s = []
visited = [False]*N

def dfs(depth):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(N):
        if depth == 0 or s[depth-1] <= L[i]:
            s.append(L[i])
            dfs(depth+1)
            s.pop()

dfs(0)