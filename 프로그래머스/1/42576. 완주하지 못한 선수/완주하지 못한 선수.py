from collections import Counter

def solution(participant, completion):
    counter = Counter(participant) - Counter(completion)
    answer = [name for name in counter]
    return answer[0]