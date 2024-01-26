# BOJ - 2667 단지번호붙이기

"""
1: 집이 있는 곳 / 0: 집이 없는 곳
연결되었다 = 좌우나 아래위로 다른 집이 있다 (대각선 X)
단지 수, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # N: 지도 한변 길이
graph = []
cnt = []

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))


def bfs(graph, a, b):
    map_len = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for index in range(4):
            nx, ny = x + dx[index], y + dy[index]
            if nx < 0 or nx >= map_len or ny < 0 or ny >= map_len:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1

    return count


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for house_cnt in cnt:
    print(house_cnt)