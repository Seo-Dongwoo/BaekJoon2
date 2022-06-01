import sys
from itertools import  permutations
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
res = 0

for per in permutations(A):
    max_sum = 0
    for i in range(N-1):
        max_sum += abs(per[i-1]-per[i])
    res = max(res, max_sum)

print(res)