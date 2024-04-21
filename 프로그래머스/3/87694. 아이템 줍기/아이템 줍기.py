from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    field = [[-1] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1
    
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    visited = [[-1] * 102 for _ in range(102)]
    queue = deque()
    queue.append([characterX*2, characterY*2])
    visited[characterX*2][characterY*2] = 0
    
    while queue:
        x, y = queue.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if field[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
    
    return answer