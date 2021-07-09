def solution(number, k):
    answer = ''
    ln = [0]
    num = 0
    for i in range(len(number)):
        while int(number[i]) > int(ln[-1]):
            ln.pop()
            k -= 1
            if k == -1 or len(ln) < 1:
                break
        ln.append(number[i])
        
        if k== -1:
            for k in range(i + 1, len(number)):
                ln.append(number[k])
            for j in range(len(ln)):
                answer = answer + ln[j]
            return answer    
    for i in range(len(ln)-1):
        if ln[i]<ln[i+1]:
            ln.pop(i)
            k -= 1
            i = -1
        if k == -1:
            for j in range(len(ln)):
                answer = answer + ln[j]
            return answer
    while k != -1:
        num += 1
        k -= 1
    
    for j in range(len(ln)-num):
        answer = answer + ln[j]
    return answer
