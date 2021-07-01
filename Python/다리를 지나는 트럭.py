def solution(bridge_length, weight, truck_weights):
    
    bridge = [0] * bridge_length
    total = len(truck_weights)
    out = 0
    time = 0
    
    while out < total:
        if bridge.pop(0) != 0:
            out += 1
        if len(truck_weights) != 0:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        else:
            bridge.append(0)
        time += 1
    
    answer = time
    return answer
