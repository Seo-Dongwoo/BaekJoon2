arr = []
sum = 0

for i in range(9):
    arr.append(int(input()))
    sum += arr[i]

for j in range(9):
    for k in range(9):
        if sum - (arr[j] + arr[k]) == 100 and j != k:
            remove = {arr[k], arr[j]}

result = [m for m in arr if m not in remove]
for m in sorted(result):
    print(m)