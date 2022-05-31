import sys
N, M = map(int, sys.stdin.readline().split())
L = sorted(map(int, sys.stdin.readline().split()))

from itertools import  combinations
combs = combinations(L, M)

for comb in combs:
    print(' '.join(map(str, list(comb))))