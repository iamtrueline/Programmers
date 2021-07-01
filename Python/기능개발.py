def solution(progresses, speeds):
    answer = []
    
    
    while len(progresses) != 0:
        sumnum = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                sumnum += 1
            else:
                break
        for i in range(sumnum):
            del progresses[0]
            del speeds[0]
        if sumnum != 0:
            answer.append(sumnum)
    
    return answer
