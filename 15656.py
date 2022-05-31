import sys
N, M = map(int, sys.stdin.readline().split())
L = sorted(map(int, sys.stdin.readline().split()))
visited = [0]*N
s = []

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, s)))
        return
    for i in range(N):
        s.append(L[i])
        dfs(depth+1)
        s.pop()

dfs(0)