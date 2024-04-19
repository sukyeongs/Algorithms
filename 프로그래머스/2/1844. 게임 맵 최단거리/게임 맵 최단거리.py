from collections import deque

def solution(maps):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    row_cnt, col_cnt = len(maps), len(maps[0])

    visited = [[0] * col_cnt for _ in range(row_cnt)]
    queue = deque()
    queue.append([0, 0])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < row_cnt and 0 <= ny < col_cnt and maps[nx][ny] != 0):
                if (visited[nx][ny] == 0):
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
    
    if visited[row_cnt-1][col_cnt-1] == 0:
        answer = -1
    else:
        answer = visited[row_cnt-1][col_cnt-1] + 1
        
    return answer