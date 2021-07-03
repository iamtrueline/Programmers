def solution(name):
    answer = 0
    
    change = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    
    idx = 0
    while True:
        answer += change[idx]
        change[idx]=0
        left = 1
        right = 1
    
        if sum(change)== 0:
            return answer
        while change[idx- left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        
        answer += min(left, right)
        idx += -left if left < right else right
    
    return answer
