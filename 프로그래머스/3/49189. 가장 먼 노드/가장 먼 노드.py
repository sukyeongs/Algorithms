from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] * (n+1) for _ in range(n+1)]
    distance = [-1] * (n+1)
    
    for e in edge:
        node1, node2 = e[0], e[1]
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    queue = deque()
    queue.append(1)
    distance[1] = 0
    
    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            if distance[node] == -1:
                queue.append(node)
                distance[node] = distance[cur] + 1
    
    max_value = max(distance)

    for i in range(1, n+1):
        if distance[i] == max_value:
            answer += 1
    
    return answer