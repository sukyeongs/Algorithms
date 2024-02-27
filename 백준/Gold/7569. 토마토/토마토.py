# BOJ - 7569 토마토
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())  # M: 상자의 가로 칸 수, N: 상자의 세로 칸 수, H: 상자가 쌓인 높이

# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 X
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
days = 0
queue = deque()


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for index in range(6):
            nx, ny, nz = x + dx[index], y + dy[index], z + dz[index]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if tomatoes[nx][ny][nz] == 0:
                    queue.append([nx, ny, nz])
                    tomatoes[nx][ny][nz] = tomatoes[x][y][z] + 1


for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 1:
                queue.append([i, j, k])

bfs()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                days = max(days, tomatoes[i][j][k])

print(days - 1)
