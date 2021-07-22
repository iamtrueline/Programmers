def solution(n):
    st = str(n)
    li = []
    for i in range(len(st)):
        li.append(st[i])
    li = sorted(li, reverse = True)
    st = ''.join(li)
    answer = int(st)
    return answer
