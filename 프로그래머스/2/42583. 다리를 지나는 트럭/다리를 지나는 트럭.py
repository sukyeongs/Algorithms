from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    currentWeight = 0
    while queue:
        time += 1
        currentWeight -= bridge.popleft()
        if currentWeight + queue[0] <= weight:
            currentWeight += queue[0]
            bridge.append(queue.popleft())
        else:
            bridge.append(0)
    
    return time + bridge_length