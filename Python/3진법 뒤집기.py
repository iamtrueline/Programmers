def solution(n): 
    answer = 0 
    s = ""
    while n > 0:
        n, mod = divmod(n, 3)
        s = s + str(mod)
    answer = int(s, 3)
    return answer
