N = int(input())
s = list(map(int, input().split()))
cnt = 0
s.sort()

for i in range(N):
    for j in range(i+1):
        cnt += s[j]
print(cnt)