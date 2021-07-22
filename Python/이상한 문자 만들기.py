def solution(s):
    answer = ''
    odd = True
    up = s.upper()
    down = s.lower()
    for i in range(len(s)):
        if s[i] == ' ': odd = False
        if odd == True: answer += up[i]
        else : answer += down[i]
        odd = not odd
    return answer
