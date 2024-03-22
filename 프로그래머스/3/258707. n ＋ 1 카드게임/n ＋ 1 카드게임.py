from collections import deque

def check(cur, remain, target):
    remain = set(remain)
    for i in cur:
        if target - i in remain:
            cur.remove(i)
            remain.remove(target-i)
            return True
    return False


def solution(coin, cards):
    answer = 1
    n = len(cards)
    target = n + 1
    cur = deque(cards[:n//3])
    remain = deque(cards[n//3:])
    pending = []
    
    while coin >= 0 and remain:
        pending.append(remain.popleft())
        pending.append(remain.popleft())
        
        if check(cur, cur, target):
            pass
        
        elif coin >= 1 and check(cur, pending, target):
            coin -= 1
        elif coin >= 2 and check(pending, pending, target):
            coin -= 2
        else:
            break
        
        answer += 1
    
    return answer