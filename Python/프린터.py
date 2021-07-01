def solution(priorities, location):
    answer = 0
    dic = []
    total = 0
    isit = 0
    
    for i in range(len(priorities)):
        if(i == location):
            dic.append([priorities[i], 1])
        else:
            dic.append([priorities[i], 0])
            
    while(len(dic) != 0):
        for i in range(len(dic)):
            if dic[0][0] < dic[i][0]:
                dic.append(dic[0])
                del(dic[0])
                isit = 1
                break
        if isit == 0:
            total += 1
            if dic[0][1] == 1:
                return total
            del(dic[0])
        else:
            isit = 0
            
            
        
    return answer
