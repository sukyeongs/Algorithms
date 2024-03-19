def solution(edges):
    answer = [0, 0, 0, 0]
    connect_info = {}
    
    for start, end in edges:
        if start in connect_info:
            connect_info[start][1] += 1
        else:
            connect_info[start] = [0, 1]
        if end in connect_info:
            connect_info[end][0] += 1
        else:
            connect_info[end] = [1, 0]
    
    for node, edge_info in connect_info.items():
        if edge_info[0] == 0 and edge_info[1] >= 2:
            answer[0] = node
        if edge_info[0] >= 1 and edge_info[1] == 0:
            answer[2] += 1
        if edge_info[0] >= 2 and edge_info[1] == 2:
            answer[3] += 1
    
    answer[1] = connect_info[answer[0]][1] - answer[2] - answer[3]
    
    return answer