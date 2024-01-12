# BOJ - 2178 미로 탐색
import sys
from collections import deque

sys_input = sys.stdin.readline
N, M = map(int, sys_input().split())
graph = [list(map(int, ' '.join(sys_input().split()))) for _ in range(N)]

queue = deque([(0, 0)])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS - 최단 경로 문제의 경우 BFS 사용할 것
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

print(graph[N-1][M-1])
