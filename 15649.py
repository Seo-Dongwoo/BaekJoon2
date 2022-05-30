import sys
N, M = map(int, sys.stdin.readline().split())
arr = []

def f():
    if len(arr) == M:
        print(' '.join(map(str,arr)))

    for i in range(1, N+1):
        if i in arr:
            continue
        arr.append(i)
        f()
        arr.pop()

f()