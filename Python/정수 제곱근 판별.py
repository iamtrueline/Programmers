def solution(n):
    answer = -1
    for i in range(int(n/2)):
        if i*i == n:
            return (i+1)**2
    if n == 1:
        answer = 4
    return answer
