def solution(lottos, win_nums):
    answer = []
    great = 0
    no = 0
    zero = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            great += 1
        elif lottos[i] == 0:
            zero += 1
    if great+zero >= 6:
        answer.append(1)
    elif great+zero == 5:
        answer.append(2)
    elif great+zero == 4:
        answer.append(3)
    elif great+zero == 3:
        answer.append(4)
    elif great+zero == 2:
        answer.append(5)
    else:
        answer.append(6)
    if great >= 6:
        answer.append(1)
    elif great == 5:
        answer.append(2)
    elif great == 4:
        answer.append(3)
    elif great == 3:
        answer.append(4)
    elif great == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    return answer
