from collections import deque

def solution(progresses, speeds):
    answer = []
    
    day = 0
    cnt = 0
    
    pq = deque(progresses)
    sq = deque(speeds)
    
    while pq:
        if pq[0] + sq[0] * day >= 100:
            cnt += 1
            pq.popleft()
            sq.popleft()
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
    
    answer.append(cnt)
    
    return answer