import sys
N = int(sys.stdin.readline())
graph = []
cnt = 0 # 총 단지수
house=0 # 단지별 속하는 집의 수
ans=[] # 리스트로 단지별 속하는 집의 수를 저장

def dfs(x,y):
    global house
    # 탐색하는 집이 그래프는 넘어갈 경우
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    
    # 탐색하는 집이 1일 경우
    if graph[x][y] == 1:
        house += 1
        # 방문했으니까 다시 0 처리
        graph[x][y] = 0

        # 상하좌우 탐색
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    # 단지로 묶여서 True값으로 반환되고 탐색했으니깐 False로 반환
    return False

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))
        
for i in range(N):
    for j in range(N):
        if dfs(i,j) == True: # 단지별로 묶여서 True로 반환
            cnt += 1 # 단지 수 증가
            ans.append(house)
            house = 0 # 다음 단지에서 집의 수를 세야하기 때문에 리셋

ans.sort()
print(cnt)
for i in ans:
    print(int(i))
            