# BOJ - 1260 DFS와 BFS

import sys
from collections import deque

sys_input = sys.stdin.readline

node_cnt, edge_cnt, start = map(int, input().split())
graph = [[] for _ in range(node_cnt + 1)]
visited_dfs = [0] * (node_cnt + 1)
visited_bfs = [0] * (node_cnt + 1)

for edge in range(edge_cnt):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(len(graph)):
    graph[i].sort()
    

def dfs(graph, visited, start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)


def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, visited_dfs, start)
print()
bfs(graph, visited_bfs, start)
