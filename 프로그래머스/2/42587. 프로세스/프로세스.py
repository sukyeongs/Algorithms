from collections import deque

def solution(priorities, location):
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    answer = 0
    
    while True:
        item = queue.popleft();
        if any(item[0] < p[0] for p in queue):
            queue.append(item)
        else:
            answer += 1
            if item[1] == location:
                return answer
            