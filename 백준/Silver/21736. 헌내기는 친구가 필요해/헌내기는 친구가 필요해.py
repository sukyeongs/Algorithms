# BOJ - 21736 헌내기는 친구가 필요해
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())  # 대학 캠퍼스 크기: N * M
graph = []
count = 0

for _ in range(N):
    graph.append(list(input().rstrip()))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(x, y):
    global count
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 'X'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] == 'X':
                continue
            else:
                queue.append([nx, ny])
                if graph[nx][ny] == 'P':
                    count += 1
                graph[nx][ny] = 'X'


for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            bfs(i, j)

if count == 0:
    print('TT')
else:
    print(count)
    