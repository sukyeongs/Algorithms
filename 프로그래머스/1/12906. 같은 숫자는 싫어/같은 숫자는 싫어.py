def solution(arr):
    answer = []
    answer.append(arr[0])
    preNum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] != preNum:
            preNum = arr[i]
            answer.append(arr[i])
    return answer