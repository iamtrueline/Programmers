def solution(d, budget):
    answer = 0
    sum = 0
    d = sorted(d)
    for i in range(len(d)):
        if sum + d[i] > budget:
            break
        else:
            sum += d[i]
            answer += 1
    return answer
