# BOJ - 10026 적록색약
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())  # 그리드 한 변 길이
painting = [list(input().rstrip()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
cnt = 0

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def no_color_blindness(i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for index in range(4):
            nx, ny = x + dx[index], y + dy[index]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] is False and painting[x][y] == painting[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])


def color_blindness(i, j):
    queue = deque()
    queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for index in range(4):
            nx, ny = x + dx[index], y + dy[index]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] is False:
                if painting[x][y] == painting[nx][ny] or (painting[x][y] in {'R', 'G'} and painting[nx][ny] in {'R', 'G'}):
                    visited[nx][ny] = True
                    queue.append([nx, ny])


for i in range(N):
    for j in range(N):
        if visited[i][j] is False:
            cnt += 1
            no_color_blindness(i, j)

print(cnt, end=' ')
cnt = 0
visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] is False:
            cnt += 1
            color_blindness(i, j)

print(cnt)
