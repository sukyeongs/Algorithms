# [Prefix Sums] PassingCars (Easy)

def solution(A):
    eastCount = 0
    result = 0

    for i in A:
        if i == 0:
            eastCount += 1
        else:
            result += eastCount
    
    if result > 1000000000:
        return -1
    
    return result