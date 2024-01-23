# BOJ - 2606 바이러스
import sys

sys_input = sys.stdin.readline

com_cnt = int(sys_input())  # 컴퓨터 수(100 이하인 양의 정수)
edge_cnt = int(sys_input())  # 연결 수

graph = [[] for _ in range(com_cnt + 1)]
visited = [False] * (com_cnt + 1)
virus_cnt = 0

for _ in range(edge_cnt):
    com1, com2 = map(int, sys_input().split())
    graph[com1].append(com2)
    graph[com2].append(com1)


def dfs(graph, visited, v):
    global virus_cnt
    visited[v] = True
    virus_cnt += 1

    for node in graph[v]:
        if not visited[node]:
            dfs(graph, visited, node)


dfs(graph, visited, 1)
print(virus_cnt-1)
