answer = 0

def dfs(numbers, target, cur, depth):
    global answer
    
    if depth == len(numbers):
        if cur == target:
            answer += 1
        return
    
    dfs(numbers, target, cur + numbers[depth], depth + 1)
    dfs(numbers, target, cur - numbers[depth], depth + 1)
    

def solution(numbers, target):
    global answer
    
    dfs(numbers, target, numbers[0], 1)
    dfs(numbers, target, -numbers[0], 1)
    
    return answer