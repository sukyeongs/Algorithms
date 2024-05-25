answer = 0

def dfs(numbers, target, cur, depth):
    global answer
    if depth == len(numbers):
        if target == cur:
            answer += 1
        return
    
    dfs(numbers, target, cur + numbers[depth], depth + 1)
    dfs(numbers, target, cur - numbers[depth], depth + 1)


def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer