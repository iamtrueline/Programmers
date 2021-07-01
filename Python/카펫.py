def solution(brown, yellow):
    answer = []
    
    slit = (int)(brown / 2 - 2);
    row = 0;
    col = 0;
    
    for i in range(1, slit):
        if i * (slit - i) == yellow:
            if i <= slit - i:
                col = slit - i
                row = i
            else:
                row = slit - i
                col = i
            break
    answer.append(col + 2)
    answer.append(row + 2)
    
    
    return answer
