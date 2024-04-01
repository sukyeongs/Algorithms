from collections import defaultdict
from itertools import product

def solution(clothes):
    answer = 1
    
    clothes_info = defaultdict(list)
    for item, category in clothes:
        clothes_info[category].append(item)
    
    if len(clothes_info.keys()) == 1:
        for value in clothes_info.values():
            return len(value)

    
    for value in clothes_info.values():
        answer *= len(value) + 1
    
    return answer - 1
    
    
