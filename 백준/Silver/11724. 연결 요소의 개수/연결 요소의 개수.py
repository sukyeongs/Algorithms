# BOJ - 11724 연결 요소의 개수
import sys
from collections import deque

sys_input = sys.stdin.readline

node_cnt, edge_cnt = map(int, sys_input().split())
graph = [[] for _ in range(node_cnt + 1)]
visited = [False] * (node_cnt+1)
count = 0

for _ in range(edge_cnt):
    node1, node2 = map(int, sys_input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)


for i in range(1, node_cnt + 1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            bfs(i)
            count += 1

print(count)