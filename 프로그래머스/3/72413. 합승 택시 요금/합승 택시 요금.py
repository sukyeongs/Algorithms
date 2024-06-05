INF = 1e9

def fillGraph(n, fares):
    graph = [[INF]*(n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        graph[i][i] = 0
        
    for s, d, f in fares:
        graph[s][d] = f
        graph[d][s] = f
    
    return graph


def floydWarshall(graph, n):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

                
def solution(n, s, a, b, fares):
    graph = fillGraph(n, fares)
    floydWarshall(graph, n)
    
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, graph[s][i]+graph[i][a]+graph[i][b])
    
    return answer