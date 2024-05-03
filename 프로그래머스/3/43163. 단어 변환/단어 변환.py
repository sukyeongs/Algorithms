answer = 0

def dfs(cur, target, words, visited, depth):
    global answer
    # 일치하는 경우 depth return
    if cur == target:
        if answer == 0 or answer > depth:
            answer = depth
        return
    
    # 일치하지 않는데 모든 단어를 탐색한 경우 0 return
    if depth == len(words):
        answer = 0
        return
    
    # 아직 전체 단어 순회를 하지 않은 경우, 차이가 1인 단어로 변경
    for i in range(len(words)):
        if calc_diff(cur, words[i]) == 1 and visited[i] == False:
            visited[i] = True
            dfs(words[i], target, words, visited, depth + 1)
            visited[i] = False

            
def calc_diff(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt
    

def solution(begin, target, words):  
    global answer
    visited = [False] * len(words)
    dfs(begin, target, words, visited, 0)
    
    return answer