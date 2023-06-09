# [Array] CyclicRotation (Easy)

def solution(A, K):
    if A:
        for i in range(K):
            shift = A.pop()
            A.insert(0, shift)
    
    return A