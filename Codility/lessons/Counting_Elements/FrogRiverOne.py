# [Counting Elements] FrogRiverOne (Easy)

def solution(X, A):
    fallLeaves = set()
    time = 0

    for i in range(len(A)):
        if A[i] not in fallLeaves:
            fallLeaves.add(A[i])
            time = i

    if len(fallLeaves) == X:
        return time

    else:
        return -1