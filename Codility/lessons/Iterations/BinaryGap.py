# [Iterations] BinaryGap (Easy)

def solution(N):
    binary = format(N, 'b')
    
    curCnt = 0
    maxCnt = 0

    for i in binary:
        if i == '1':
            if curCnt > maxCnt:
                maxCnt = curCnt
            curCnt = 0
        
        else:
            curCnt += 1   

    return maxCnt
