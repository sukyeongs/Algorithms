# BOJ - 7576 토마토
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())  # M: 상자의 가로 칸 수, N: 상자의 세로 칸 수
tomatoes = [list(map(int, input().split())) for _ in range(N)]  # 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 ㅌ
queue = deque()
day = 0

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append([i, j])

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append([nx, ny])


bfs()
for tomato in tomatoes:
    for i in tomato:
        if i == 0:
            print(-1)
            exit(0)
    day = max(day, max(tomato))

print(day - 1)

"""
문제에서 '인접한 토마토', '최소 일수'라는 키워드를 작성한 것으로 보아 이는 bfs를 활용하는 문제임을 알 수 있다.
dfs를 사용할 필요가 없다. (깊이 탐색하는 것X)
"""