def dfs(graph, visited, v):
    visited[v] = True
    
    for node in graph[v]:
        if not visited[node]:
            visited[node] = True
            dfs(graph, visited, node)
            
    return visited
    
def solution(n, computers):
    answer = 0
    visited = [False] * n
    graph = [[] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    
    for i in range(n):
        if not visited[i]:
            visited = dfs(graph, visited, i)
            answer += 1
        
    return answer