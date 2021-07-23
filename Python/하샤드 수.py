def solution(x):
    sum = 0
    s = str(x)
    for i in range(len(s)):
        sum += int(s[i])
    if x%sum == 0:
        answer = True
    else:
        answer = False
    return answer
