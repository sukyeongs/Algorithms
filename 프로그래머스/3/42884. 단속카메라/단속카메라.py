def solution(routes):
    routes.sort(key = lambda x : x[1])
    compare = routes[0][1]
    answer = 1
    
    for route in routes:
        if route[0] <= compare <= route[1]:
            continue
        if route[0] > compare:
            compare = route[1]
            answer += 1

    return answer