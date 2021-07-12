def solution(board, moves):
    answer = 0
    toy = []
    
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                toy.append(board[j][moves[i]-1])
                if len(toy)>=2 and toy[-1] == toy[-2]:
                    answer += 2
                    toy.pop()
                    toy.pop()
                board[j][moves[i]-1] = 0
                break
    
    return answer
