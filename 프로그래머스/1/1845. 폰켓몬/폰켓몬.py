def solution(nums):
    n = len(nums)  # 포켓몬 수
    pocketmon = set(nums)
    
    if len(pocketmon) >= n//2:
        return n//2
    
    if n//2 == 1:
        return 1
    
    return len(pocketmon)
