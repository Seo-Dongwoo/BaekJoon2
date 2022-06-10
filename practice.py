import sys
N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
cnt = 0
house = 0
house_list= []

def dfs(x,y):
    global house
    if x < 0 or x > N or y < 0 or y > N:
        return False

        # 탐색하는 집이 1일 경우
    if graph[x][y] == 1:
        house += 1
        # 방문했으니까 다시 0 처리
        graph[x][y] = 0

        # 상하좌우 탐색
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
        # 단지로 묶여서 True값으로 반환되고 탐색했으니깐 False로 반환
    return False

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:  # 단지별로 묶여서 True로 반환
            cnt += 1  # 단지 수 증가
            house_list.append(house)
            house = 0  # 다음 단지에서 집의 수를 세야하기 때문에 리셋

house_list.sort()
print(cnt)
for i in house_list:
    print(int(i))
