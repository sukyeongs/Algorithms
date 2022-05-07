# 1260 - DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)

for i in range(m):
  c1, c2 = map(int, input().split())
  graph[c1].append(c2)
  graph[c2].append(c1)

for i in range(len(graph)):
  graph[i].sort()

def dfs(graph, v, visited):
  visited[v] = 1
  print(v, end= ' ')
  for i in graph[v]:
    if visited[i] == 0:
      visited[i] = 1
      dfs(graph, i, visited)

def bfs(graph, v, visited):
  queue = deque([v])
  visited[v] = 1
  while queue:
    q = queue.popleft()
    print(q, end=' ')
    for i in graph[q]:
      if visited[i] == 0:
        queue.append(i)
        visited[i] = 1
  

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)
