# [Time Complexity] FrogJmp (Easy)

def solution(X, Y, D):
    leftDistance = (Y - X)
    cnt = leftDistance // D
    remainder = leftDistance % D

    if remainder == 0:
        return cnt
    else:
        return cnt + 1