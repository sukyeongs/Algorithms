def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) 
    visited = set([costs[0][0]])

    while len(visited) != n:
        for v in costs:
            if v[0] in visited and v[1] in visited:
                continue
            if v[0] in visited or v[1] in visited:
                visited.update([v[0], v[1]])
                answer += v[2]
                break

    return answer