from collections import deque

def bfs(graph, visited, v):
    queue = deque()
    queue.append(v)
    
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
    
    return visited
    

def solution(n, computers):
    answer = 0
    
    graph = [[] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            visited = bfs(graph, visited, i)
            answer += 1
    
    return answer