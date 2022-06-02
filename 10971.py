import sys
N = int(sys.stdin.readline()) #도시 개수
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_value = sys.maxsize # 출력할 최소값 정의

def dfs(start, next, value, visited): #(시작 도시, 다음 도시, 비용, 방문 여부)
    global min_value

    if len(visited) == N: # 방분 도시가 입력받은 도시 개수라면
        if cost[next][start] != 0: # 마지막 도시에서 처음 도시로 가는 비용이 0이라면
            min_value = min(min_value, value+cost[next][start]) # 더한 값을 저장되어 있는 최솟값과 비교해서 대입
        return

    for i in range(N):
        if cost[next][i] != 0 and i not in visited and value < min_value:
            # 다음 도시로 가는 비용이 0이 아니고 방문을 하지 않았고 그 비용값이 저장되어있는 최소값보다 작다면
            visited.append(i) # 방문한걸로 취급하고
            dfs(start, i, value+cost[next][i], visited) # 그 도시 방문
            visited.pop() # 방문한거 해제

for i in range(N):
    dfs(i, i, 0, [i])

print(min_value)