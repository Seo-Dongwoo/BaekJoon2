N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost = costs[0]
sum = 0
for i in range(N-1):
    if min_cost > costs[i]:
        min_cost = costs[i]
    sum += (min_cost * roads[i])
print(sum)
