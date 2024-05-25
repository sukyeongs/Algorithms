from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for src, dst in tickets:
        graph[src].append(dst)
    
    for src in graph:
        graph[src].sort(reverse=True)

    answer = []
    stack = ["ICN"]
    
    while stack:
        cur = stack[-1]
        if not graph[cur]:
            answer.append(stack.pop())
        else:
            stack.append(graph[cur].pop())
    
    return answer[::-1]