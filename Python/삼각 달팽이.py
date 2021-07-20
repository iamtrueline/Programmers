def solution(n):
    answer = []
    res = [[0 for _ in range(n)]for _ in range(n)]
    y = -1
    x = 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i%3 == 0:   
                y +=1
            elif i%3 == 1:
                x+= 1
            elif i%3 == 2:
                y -=1
                x -=1
            res[y][x] = num
            num += 1
    for i in range(n):
        for j in range(n):
            if res[i][j] != 0:
                answer.append(res[i][j])
    return answer
