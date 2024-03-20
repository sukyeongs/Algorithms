from collections import deque

def solution(queue1, queue2):
    answer = -1
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    total = sum1 + sum2
    
    if total % 2 != 0:
        return answer

    cnt = 0
    goal = total // 2
    limit = len(queue1) * 4
    
    while True:
        if sum1 == sum2:
            break
        if cnt >= limit:
            cnt = -1
            break
        else:
            if sum1 > sum2:
                data = queue1.popleft()
                if data > goal:
                    cnt = -1
                    break
                else:
                    sum1 -= data
                    queue2.append(data)
                    sum2 += data
            else:
                data = queue2.popleft()
                if data > goal:
                    cnt = -1
                    break
                else:
                    sum2 -= data
                    queue1.append(data)
                    sum1 += data
            cnt += 1

    return cnt