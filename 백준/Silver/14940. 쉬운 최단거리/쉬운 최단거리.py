# BOJ - 14940 쉬운 최단거리
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())  # n: 세로 길이, m: 가로 길이
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if visited[i][j] == -1 and graph[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if visited[i][j] != -1:
            print(visited[i][j], end=' ')
        else:
            print(0, end=' ') if graph[i][j] == 0 else print(-1, end=' ')
    print()
    