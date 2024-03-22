def can_build(answer):
    for x, y, a in answer:
        # 기둥
        if a == 0:
            if (y != 0 and
                [x, y - 1, 0] not in answer and
                [x - 1, y, 1] not in answer and
                [x, y, 1] not in answer):
                return False
        # 보
        else:
            if ([x, y - 1, 0] not in answer and
                [x + 1, y - 1, 0] not in answer and
                ([x - 1, y, 1] not in answer or 
                 [x + 1, y, 1] not in answer)
               ):
                return False
    return True
        

def solution(n, build_frame):
    answer = []
    
    for x, y, a, b in build_frame:
        # 삭제인 경우
        if b == 0:
            answer.remove([x, y, a])
            # 조건 성립 안 되면 다시 추가
            if not can_build(answer):
                answer.append([x, y, a])
        # 추가인 경우
        else:
            answer.append([x, y, a])
            # 조건 성립 안 되면 다시 삭제
            if not can_build(answer):
                answer.remove([x, y, a])
    
    answer.sort(key = lambda x: (x[0], x[1], x[2]))
    return answer