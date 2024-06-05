from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combination = combinations(sorted(order), c)
            temp += combination

        counter = Counter(temp)
        max_value = max(counter.values()) if len(counter) > 0 else 0
        
        if len(counter) > 0 and max_value > 1:
            answer += [''.join(f) for f in counter if counter[f] == max_value]
    
    return sorted(answer)