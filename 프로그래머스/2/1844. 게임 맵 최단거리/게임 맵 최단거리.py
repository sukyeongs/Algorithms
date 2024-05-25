from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1
    
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    
    if visited[n-1][m-1] != 0:
        return visited[n-1][m-1]
    
    return -1