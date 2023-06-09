# [Arrays] OddOccurrencesInArray (Easy)

import collections

def solution(A):
    cntDict = collections.Counter(A)

    for val, cnt in cntDict.items():
        if cnt % 2 == 1:
            return val
