def solution(s):
    answer = ''
    lenn = len(s)
    if lenn%2==0:
        answer = s[int(lenn/2-1)] + s[int(lenn/2)]
    else:
        answer = s[int(lenn/2)]
    
    return answer
