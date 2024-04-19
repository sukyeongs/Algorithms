def dfs(graph, visited, cur):
    visited[cur] = True
    for node in graph[cur]:
        if not visited[node]:
            visited[node] = True
            dfs(graph, visited, node)

def solution(n, computers):
    answer = 0
    
    graph = [[] for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(graph, visited, i)
            
    return answer