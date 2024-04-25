import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville:
        # heap에서 가장 작은 원소가 K 이상이면 break
        if scoville[0] >= K:
            break
        # heap에 원소가 1개뿐인데 K보다 작으면 만들 수 없는 것이므로 -1 반환
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        # 섞기
        mix = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, mix)
        answer += 1
    
    return answer