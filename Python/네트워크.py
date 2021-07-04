def solution(n, computers):
    answer = 0
    
    visit = [0 for i in range(n)]
    
    for m in range(n):
        if visit[m] == 0:
            find(m, computers, n, visit)
            answer += 1
    
    return answer

def find(m, computers, n, visit):
    visit[m] = 1;
    
    for i in range(n):
        if m != i and visit[i] == 0 and computers[m][i] == 1:
            find(i, computers, n, visit)
