def solution(a, b):
    answer = ''
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    m = 0
    for i in range(a-1):
        m += month[i]
    m += b
    m %= 7
    answer = day[int(m)-1]
    return answer
