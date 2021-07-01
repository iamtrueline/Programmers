def solution(prices):
    answer = []
    idx = 0
    while idx < len(prices)-1:
        time = 0
        n = prices[idx]
        for i in range(idx + 1, len(prices)):
            if prices[i] >= n:
                time += 1
            else:
                time += 1
                answer.append(time)
                time = 0
                break
        if time != 0:
            answer.append(time)
        idx += 1
        
    answer.append(0)
    
    return answer
