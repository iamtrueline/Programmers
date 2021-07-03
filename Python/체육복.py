def solution(n, lost, reserve):
    answer = 0
    lost = sorted(lost)
    reserve = sorted(reserve)
    
    for i in range(1, n+1):
        if i in lost:
            if i in reserve:
                reserve.remove(i)
                lost.remove(i)
                answer += 1     
        else:
            answer += 1
    
    for i in range(1, n+1):
        if i in lost:
            if i - 1 in reserve:
                answer += 1
                reserve.remove(i-1)
                continue
            if i + 1 in reserve:
                answer += 1
                reserve.remove(i+1)
                continue
                
    return answer
