def solution(m, n, puddles):
    graph = [[0] * (m) for _ in range(n)]
    graph[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if [j+1, i+1] in puddles:
                graph[i][j] = 0
            else:
                graph[i][j] = (graph[i-1][j] + graph[i][j-1]) % 1000000007

    return graph[n-1][m-1]