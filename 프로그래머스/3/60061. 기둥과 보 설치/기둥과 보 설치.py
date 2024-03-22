def check(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

    
def solution(n, build_frame):
    answer = []
    graph = [[-1] * n for _ in range(n)]
    
    for build in build_frame:
        x, y, a, b = build[0], build[1], build[2], build[3]
        
        if not check(x, y, n):
            continue
        
        # 기둥
        if a == 0:
            # 기둥 삭제
            if b == 0:
                if y + 1 > n and (graph[x][y+1] == -1 or (x + 1 < n and ((graph[x+1][y+1] == 1 and graph[x][y] == 0) or graph[x+1][y+1] == 0 and graph[x][y+1] == 1))):
                                  graph[x][y] = -1
                else:
                    continue

            # 기둥 설치
            else:
                if y == 0 or (x+1 < n and graph[x+1][y] == 1) or (x-1 >= 0 and graph[x-1][y] == 1) or (y-1 >= 0 and graph[x][y-1] == 0):
                    graph[x][y] = 0
                else:
                    continue
        # 보
        else:
            # 보 삭제
            if b == 0:
                if (x+1 < n and graph[x+1][y] == 0) or (x+1 < n and x-1 >= 0 and graph[x+1][y] == 1 and graph[x-1][y] == 1):
                    continue
                else:
                    graph[x][y] = -1

            # 보 설치
            else:
                if ((y - 1 >= 0 and graph[x][y-1] == 0) or (x + 1 < n and y - 1 >= 0 and graph[x+1][y-1] == 0) or (x - 1 >= 0 and x + 1 < n and graph[x-1][y] == 1 and graph[x+1][y] == 1)):
                    graph[x][y] = 1
                else:
                    continue          
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:
                continue
            else:
                answer.append([i, j, graph[i][j]])

    return answer