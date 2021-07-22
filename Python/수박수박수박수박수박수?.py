def solution(n):
    answer = ''
    for _ in range(int(n/2)):
        answer += '수박'
    if n%2 !=0:
        answer += '수'
    return answer
