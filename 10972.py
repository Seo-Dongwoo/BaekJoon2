import sys
N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

for i in range(N-1, 0, -1):
    if L[i-1] < L[i]:
        for j in range(N-1, 0, -1):
            if L[i-1] < L[j]:
                L[i-1], L[j] = L[j], L[i-1]
                L = L[:i] + sorted(L[i:])
                print(*L)
                exit()

print(-1)

