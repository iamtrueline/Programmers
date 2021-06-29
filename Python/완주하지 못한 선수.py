def solution(participant, completion):
    go = {}
    
    for i in participant:
        if go.get(i) == None:
            go[i] = 1
        else:
            go[i] += 1
    for i in completion:
        go[i] -= 1
    
    for i, j in go.items():
        if j != 0:
            answer = i
            return answer
