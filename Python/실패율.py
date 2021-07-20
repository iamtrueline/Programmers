def solution(N, stages):
    answer = {}
    person = len(stages)
    for i in range(1, N+1):
        if person != 0:
            count = stages.count(i)
            answer[i] = count / person
            person -= count
        else:
            answer[i] = 0
    answer = sorted(answer, key=lambda x : answer[x],reverse=True)
    return answer
