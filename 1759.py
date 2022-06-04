import sys
from itertools import combinations
L, C = map(int, sys.stdin.readline().split())
lst = sorted(list(map(str, sys.stdin.readline().split())))

comb = combinations(lst, L)
moum = ['a', 'e', 'i', 'o', 'u']

for C in comb:
    j = 0
    m = 0
    for i in range(L):
        if C[i] in moum:
            m += 1
        else:
            j += 1
    if m >= 1 and j >= 2:
        print(''.join(C))