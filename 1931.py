N = int(input())
s = []
for i in range(N):
    first, second = map(int, input().split())
    s.append([first, second])

s = sorted(s, key= lambda a : a[0])
s = sorted(s, key= lambda a : a[1])
last_end = 0
cnt = 0

for first, second in s:
    if first > last_end:
        cnt += 1
        last_end = second
        
print(cnt)