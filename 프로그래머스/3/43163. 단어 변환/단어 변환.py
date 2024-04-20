from collections import deque, Counter

answer = 0

def dfs(words, target, visited, cur, depth):
    global answer

    if (cur == target):
        if answer == 0 or answer > depth:
            answer = depth

        return
    
    if (len(words) == depth and cur != target):
        answer = 0
        return

    for index, word in enumerate(words):
        if (visited[index] == 0 and len(Counter(word) - Counter(cur)) == 1):
            visited[index] = 1
            dfs(words, target, visited, word, depth + 1)
            visited[index] = 0

            
def solution(begin, target, words):    
    visited = [0] * len(words)
    dfs(words, target, visited, begin, 0)
    
    return answer