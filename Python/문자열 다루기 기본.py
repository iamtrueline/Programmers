def solution(s):
    answer = True
    
    if len(s) != 4 and len(s) != 6:
        return False
        
    for i in range(len(s)):
        if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
            return False
    
    return answer
