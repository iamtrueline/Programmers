def solution(numbers):
    answer = ''
    n = ''
    s = ''
    zero = True
    
    list = []
    
    for i in range(len(numbers)):
        if numbers[i] != 0:
            zero = False
    
    if zero == True:
        return '0'
    
    for i in range(len(numbers)):
        s = str(numbers[i])
        if numbers[i] < 10:
            n = s + s + s + s + s
        elif numbers[i] < 100:
            n = s + s + s[0]
        elif numbers[i] < 1000:
            n = s + s[0] + s[1]
        else:
            n = '10001'
        list.append([n, s])
        
    list = sorted(list, reverse=True)
    
    for i in range(len(list)):
        answer = answer + list[i][1]
    return answer
