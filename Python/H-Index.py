def solution(citations):
    answer = 0
    
    citations = sorted(citations, reverse=True)
    h = citations[0]
    j = 0
    
    while(h != 0):
        for i in range(len(citations)):
            if citations[i] < h:
                break
            else:
                j += 1
            if j >= h:
                return j
        h -= 1
        j = 0
    
    
    
    return j
