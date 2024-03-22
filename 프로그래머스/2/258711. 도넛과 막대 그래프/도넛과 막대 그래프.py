def solution(edges):
    answer = [0, 0, 0, 0]
    node_info = {}
    
    for edge in edges:
        start, end = edge[0], edge[1]
        if start in node_info:
            node_info[start][1] += 1
        else:
            node_info[start] = [0, 1]
            
        if end in node_info:
            node_info[end][0] += 1
        else:
            node_info[end] = [1, 0]
            
    for key, value in node_info.items():
        if value[0] == 0 and value[1] >= 2:
            answer[0] = key
            continue
        
        elif value[0] >= 1 and value[1] == 0:
            answer[2] += 1
        
        elif value[0] >= 2 and value[1] == 2:
            answer[3] += 1
    
    answer[1] = node_info[answer[0]][1] - answer[2] - answer[3]
    
    return answer