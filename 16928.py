from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
board = [0] * 101
visited = [False] * 101
ladder = dict()
snake = dict()

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    ladder[a] = b

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    snake[a] = b

queue = deque([1])

while queue:
    x = queue.popleft()
    if x == 100:
        print(board[x])
        break

    for dice in range(1, 7):
        next_place = x + dice
        if next_place <= 100 and not visited[next_place]:
            if next_place in ladder.keys():
                next_place = ladder[next_place]

            if next_place in snake.keys():
                next_place = snake[next_place]

            if not visited[next_place]:
                visited[next_place] = True
                board[next_place] = board[x] + 1
                queue.append(next_place)



